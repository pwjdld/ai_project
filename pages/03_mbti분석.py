# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="MBTI Country Dashboard",
    layout="wide"
)

# 제목
st.title("🌍 국가별 MBTI 비율 분석")
st.write("국가를 선택하면 MBTI 16가지 유형 비율을 그래프로 보여줍니다.")

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# 국가 선택
country = st.selectbox(
    "국가 선택",
    sorted(df["Country"].unique())
)

# 선택 국가 데이터
selected = df[df["Country"] == country].iloc[0]

# MBTI 컬럼
mbti_cols = [
    'INFJ', 'ISFJ', 'INTP', 'ISFP',
    'ENTP', 'ISTP', 'INTJ', 'ESTP',
    'ENFJ', 'ESFJ', 'INFP', 'ESFP',
    'ENFP', 'ESTJ', 'ISTJ', 'ENTJ'
]

# 값 추출
values = selected[mbti_cols].astype(float)

# 내림차순 정렬
values = values.sort_values(ascending=False)

# 색상 설정
colors = []

# 초록색 그라데이션
green_gradient = np.linspace(0.9, 0.3, len(values)-1)

idx = 0
for i, mbti in enumerate(values.index):
    if i == 0:
        colors.append("blue")
    else:
        colors.append((0, green_gradient[idx], 0))
        idx += 1

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    values.index,
    values.values,
    color=colors
)

# 값 표시
for bar in bars:
    h = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        h + 0.002,
        f"{h:.2%}",
        ha='center',
        fontsize=9
    )

# 그래프 스타일
ax.set_title(f"{country} MBTI 비율", fontsize=18)
ax.set_xlabel("MBTI 유형")
ax.set_ylabel("비율")

plt.xticks(rotation=45)
plt.tight_layout()

# 출력
st.pyplot(fig)

# 최고 MBTI
top_mbti = values.index[0]
top_value = values.iloc[0]

st.success(
    f"🏆 {country}에서 가장 높은 MBTI는 "
    f"'{top_mbti}' ({top_value:.2%}) 입니다."
)

# 데이터 테이블
st.subheader("📋 MBTI 데이터")

table_df = pd.DataFrame({
    "MBTI": values.index,
    "비율": [f"{v:.2%}" for v in values.values]
})

st.dataframe(table_df, use_container_width=True)
