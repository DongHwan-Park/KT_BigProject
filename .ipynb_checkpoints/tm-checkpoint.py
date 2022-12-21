# streamlit, pandas 라이브러리 불러오기 
import streamlit as st
import pandas as pd

 

# 꽉 찬 화면
st.set_page_config(layout="wide")

 

# 데이터 가져오기
dt = pd.read_csv('train.csv')

 

# multipage
# 페이지 선언
def page1():
    st.title('직원용 웹사이트')
    st.sidebar.title('직원용 웹사이트')
    st.markdown('#### 차액 기준 내림차순 고객 리스트')
    st.dataframe(dt)

    st.markdown('#### 고객 검색(주소 및 위치 기반)')
    cust = st.text_input('입력칸') # 유저한테 글자 입력받기
    st.markdown(cust)
    st.markdown('#### 고객 연락수단(email 전송, sns 연동 등)')

def page2():
    st.title('고객용 웹사이트')
    st.sidebar.title('고객용 웹사이트')

    new_title = '<p style="font-family:Malgun Gothic; color:blue; font-size: 42px;">캐치 프레이즈</p>'
    st.markdown(new_title, unsafe_allow_html=True)
    # st.info() # 파란색 영역
    # st.success() # 녹색 영역
    # st.warning() # 노란색 영역
    # st.error() # 레드 영역

    st.markdown('#### 아래 양식에 맞게 정보를 입력해주세요.')
    st.markdown('**단지명  |  전용면적(㎡)  |  층수  |  도로명 주소**')
    st.text_input('예시) 명동교자  | 100  |  1  | 중구 명동10길 29') # 유저한테 글자 입력받기

    st.markdown('#### 메인지표 3가지')
    st.metric(label="예측된 일일가격", value="60,000won", delta="20,000won")
    main=dt['일일가격'][:10]
    st.bar_chart(main)

    st.markdown('#### 외부지표 6가지')

# 딕셔너리 선언 { ‘selectbox항목’ : 페이지명… }
page_names_to_funcs = {'page1': page1, 'page2': page2}

# 사이드 바에 selectbox 선언
selected_page = st.sidebar.selectbox('Select a page', page_names_to_funcs.keys())

# 페이지 함수 부르기
page_names_to_funcs[selected_page]()