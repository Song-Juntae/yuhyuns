import streamlit as st
import pandas as pd

# 레이아웃

with st.container():
    col_0_0, col_0_1, col_0_2, col_0_3 = st.columns([1,1,1,1])

with st.container():
    col_1_0, col_1_1, col_1_2, col_1_3 = st.columns([1,1,1,1])

with st.container():
    col_2_0, col_2_1, col_2_2, col_2_3 = st.columns([1,1,1,1])

# 데이터 로드

from pathlib import Path

print(Path.cwd())

df = pd.read_csv('/app/song-juntae/yuhyuns/data/날짜별_가게별_카테모리매출합.csv')

# 시각화
df