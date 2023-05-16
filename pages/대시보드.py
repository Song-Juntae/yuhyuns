import streamlit as st
import pandas as pd

import plotly.graph_objects as go

# 레이아웃

with st.container():
    col_0_0, col_0_1, col_0_2, col_0_3 = st.columns([1,1,1,1])

with st.container():
    col_1_0, col_1_1, col_1_2, col_1_3 = st.columns([1,1,1,1])

with st.container():
    col_2_0, col_2_1, col_2_2, col_2_3 = st.columns([1,1,1,1])

# 데이터 로드
df = pd.read_csv('/app/yuhyuns/data/날짜별_가게별_카테모리매출합.csv')

# 시각화

with col_1_0:
    options = st.multiselect(
        '가게 번호를 선택해주세요.',
        [1,2,3,4,5,6,7,8,9,10],
        [1, 2])
    
    st.write('가게 번호:', options)
    가게25번카테고리매출합 = pd.DataFrame(df.iloc[:,2:][df['store_nbr'] == options].dropna().sum()).sort_values(0, ascending=False)
    가게25번카테고리매출합 = 가게25번카테고리매출합.reset_index()
    가게25번카테고리매출합.columns = ['카테고리','매출합']

    fig = go.Figure([go.Bar(x=가게25번카테고리매출합['카테고리'], y=가게25번카테고리매출합['매출합'])])
    fig