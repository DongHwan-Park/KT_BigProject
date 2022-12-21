import streamlit as st
import pandas as pd
import numpy as np
import joblib
import pydeck as pdk
import urllib.request
import json

# 노드 정보 로드
node = pd.read_csv('node.csv', index_col=0)

# 링크 정보 로드
link = pd.read_csv('link.csv', index_col=0)
link['node_s'] = link['node_s'].astype(str)
link['node_d'] = link['node_d'].astype(str)

# 집회 위도, 경도 정보    
assembly = pd.read_csv('assembly.csv')
assembly_info = assembly[:]
assembly['name'] = '신고인원 : ' + assembly['신고인원'] + '(명)'
assembly = assembly.loc[:,['위도', '경도', 'name']]

assembly['위도'] = assembly['위도'].astype(float)
assembly['경도'] = assembly['경도'].astype(float)

assembly.columns = ['lat', 'lng', 'name']
assembly = assembly[['lng', 'lat', 'name']]

# 돌발 정보
key = 'ee7ce15c2ead4ea5871c3dc8f1a198f5'
minX, maxX = 126.734086, 127.269311
minY, maxY = 37.413294, 37.715133

url = f'https://openapi.its.go.kr:9443/eventInfo?apiKey={key}&type=all&eventType=all&minX={minX}&maxX={maxX}&minY={minY}&maxY={maxY}&getType=json'
response = urllib.request.urlopen(url)
json_str = response.read().decode('utf-8')
json_obj = json.loads(json_str)

outbreak = pd.json_normalize(json_obj['body']['items'])
outbreak_info = outbreak[:]

outbreak.loc[outbreak['eventType']=='공사', 'eventDetailType'] = '공사'
outbreak = outbreak.loc[:, ['coordX', 'coordY', 'eventDetailType']]
outbreak.columns = ['lng', 'lat', 'name']

outbreak['lng'] = outbreak['lng'].astype(float)
outbreak['lat'] = outbreak['lat'].astype(float)

layer_assembly = pdk.Layer(
    'ScatterplotLayer',
    assembly,
    get_position='[lng, lat]',
    get_radius=50,
    get_fill_color='[255, 212, 0]',
    pickable=True,
    auto_highlight=True
)

layer_outbreak = pdk.Layer(
    'ScatterplotLayer',
    outbreak,
    get_position='[lng, lat]',
    get_radius=50,
    get_fill_color='[255, 0, 0]',
    pickable=True,
    auto_highlight=True
)

# 지도 기본 설정
layers=[layer_outbreak, layer_assembly]
# layers=[layer_assembly]
view_state = pdk.ViewState(
    latitude=37.5702,
    longitude=126.9753,
    zoom=14
)

# 아이콘 정보
icon_data = {
    "url": 'icon.png',
    "width": 128,
    "height":128,
    "anchorY": 128
}

# 출발,도착 지점 입력
col1, col2 = st.columns(2)
with col1:
    in1 = st.selectbox("출발지",
                       sorted(list(node['node'].unique())+['']),
                       help='현재 [신문로1가141]선택 시에만 정상적으로 처리됩니다')
with col2:
    in2 = st.selectbox("도착지",
                       sorted(list(node['node'].unique())+['']),
                       help='현재 [SK빌딩]선택 시에만 정상적으로 처리됩니다')

if in1:
    tmp = node.loc[node['node']==str(in1), :]
    tmp['name'] = '출발지'
    layer_from = pdk.Layer(
        type='ScatterplotLayer',
        data=tmp,
        get_position='[lng, lat]',
        get_radius=50,
        get_fill_color='[0, 128, 0]',
        pickable=True,
        auto_highlight=True
    )
    layers.append(layer_from)

if in2:
    tmp = node.loc[node['node']==str(in2), :]
    tmp['name'] = '도착지'
    layer_to = pdk.Layer(
        type='ScatterplotLayer',
        data=tmp,
        get_position='[lng, lat]',
        get_radius=50,
        get_fill_color='[150, 75, 0]',
        pickable=True,
        auto_highlight=True
    )
    layers.append(layer_to)
    
tmp = node.loc[(round(node['lat'],4)==37.5702) & (node['lng']<126.9820) & (126.9756 <= node['lng']), ['lng', 'lat']]
tmp.reset_index(drop=True, inplace=True)
geo = '['
for idx, row in tmp.iterrows():
    ret = [row['lng'], row['lat']]
    geo += str(ret)
    geo +=', '
    
geo = geo[:-2] + ']'

def line2coor(d):
    g = []
    for i in range(len(tmp)):
        lng, lat = tmp.loc[i,'lng'], tmp.loc[i,'lat']
        g.append([lng,lat])
    return g

path = pd.DataFrame({
    'name':'route',
    'geometry':geo
}, index=[0])
path['geometry'] = path['geometry'].apply(line2coor)
path = pd.DataFrame(path)

# 예측 시간 정보 표현
model = joblib.load('./travelTimeModel.pkl')
avgTT = pd.read_csv('./link_avgTT.csv')
avgTT['travelTime'].fillna(avgTT.loc[avgTT['travelTime'].notnull(), 'travelTime'].mean(), inplace=True)
if in1!='' and in2!='':
    target_link = link.loc[(link['node_s']==str(in1)) & (link['node_d']==str(in2)), 'linkId']
    avg, pred = 0, 0
    path_link = ['1000001002','1000001003', '1000001401','1000001402','1000001403','1000000301']
    for pl in path_link:
        try:
            a = avgTT.loc[avgTT['linkId'] == float(pl), 'travelTime'].values[0]
        except:
            a = avgTT['travelTime'].mean()
        p = model.predict(np.array([float(pl), 0, 0, 2]).reshape(1,-1))[0]
        print(a)
        avg += a
        pred += p

    st.subheader(f'예상 소요 시간 : {pred:.2f} (초)')
    st.subheader(f'예상 지연 시간 : {abs(pred-avg):.2f} (초)')
    
    layer_path = pdk.Layer(
        type='PathLayer',
        data=path,
        pickable=True,
        get_color='[255, 255, 255]',
        width_scale=5,
        width_min_pixels=2,
        get_path='geometry',
        get_width=5
    )
    layers.append(layer_path)

r = pdk.Deck(layers=layers, initial_view_state=view_state, tooltip={'text': '{name}'})
st.pydeck_chart(r)

st.header('집회 정보')
assembly_info = assembly_info.loc[:, ['날짜', '요일', '위치', '신고인원']]
st.dataframe(assembly_info)
st.header('돌발 정보')
outbreak_info = outbreak_info.loc[outbreak_info['roadName']!='', ['roadName', 'eventType', 'eventDetailType', 'message', 'endDate']]
st.dataframe(outbreak_info)