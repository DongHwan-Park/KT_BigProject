{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7ad4160-4318-4ef4-87bd-ccc1173c3c35",
   "metadata": {},
   "outputs": [],
   "source": [
    "# !pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "f6ebd541-9f43-4d7a-8bd1-a5a28266a70b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8125c51f-2f91-4895-a433-37d77d3eedf2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# streamlit, pandas 라이브러리 불러오기 \n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "# header, subheader, text, caption 연습하기\n",
    "st.title('Text elements')\n",
    "# st.caption('text 참고사이트: https://docs.streamlit.io/library/api-reference/text')\n",
    "# st.header('Header: 데이터 분석 표현')\n",
    "# st.subheader('Subheader: 스트림릿')\n",
    "# st.text('Text: this is the Streamlit')\n",
    "# st.caption('Caption: Streamlit은 2019년 하반기에 등장한 파이썬 기반의 웹어플리케이션 툴이다')\n",
    "\n",
    "# # markdown 연습하기\n",
    "# st.markdown('# Markdown ')\n",
    "# st.markdown('## Markdown')\n",
    "# st.markdown('### Markdown')\n",
    "# st.markdown('**_Markdown_**')\n",
    "# st.markdown('- **_Markdown_**')\n",
    "\n",
    "# # Latex & Code 연습하기\n",
    "# st.markdown('## Code & Latex')\n",
    "# st.code('a + ar + ar^2 + ar^3')\n",
    "# st.latex(r'''a + ar + ar^2 + ar^3''') \n",
    "\n",
    "# # write 연습하기\n",
    "# st.title('write')\n",
    "# st.caption('참고사이트: https://docs.streamlit.io/library/api-reference/write-magic/st.write')\n",
    "# st.text('아래 딕셔너리를 판다스 데이터프레임으로 변경')\n",
    "# st.caption(\"{'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']}\")\n",
    "# df = pd.DataFrame({'이름': ['홍길동', '김사랑', '일지매', '이루리'],'수준': ['금', '동', '은', '은']})\n",
    "# st.write('딕셔너리를 판다스의 데이터프레임으로 바꿔서', df, '스트림릿의 write 함수로 표현')\n",
    "\n",
    "# 파일실행: File > New > Terminal(anaconda prompt) - streamlit run 파이썬파일명"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b67ed4f3-0b66-41a2-98a8-85cce10c9ccb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
