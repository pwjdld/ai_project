# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="MBTI Top 10 Countries",
    layout="wide"
)

st.title("🌍 MBTI 유형별 상위 10개 국가")
st.write("MBTI 유형을 선택하면 해당 비율이 가장 높은 국가 10개를 보여줍니다.")

# 데이터 불러오기
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# MBTI 목록
mbti_types = [
    'INFJ', 'ISFJ', 'INTP', 'ISFP',
    'ENTP', 'ISTP', 'INTJ', 'ESTP',
    'ENFJ', 'ESFJ', 'INFP', 'ESFP',
    'ENFP', 'ESTJ', 'ISTJ', 'ENTJ'
]

# MBTI 선택
selected_mbti = st.selectbox(
    "MBTI 유형 선택",
    mbti_types
)

# 상위 10개 국가 추출
top10 = df[['Country', selected_mbti]] \
    .sort_values(by=selected_mbti, ascending=False) \
    .head(10)

# 색상 설정
colors = ['blue']

green_gradient = np.linspace(0.85, 0.35, 9)

for g in green_gradient:
    colors.append((0, g, 0))

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    top10['Country'],
    top10[selected_mbti],
    color=colors
)

# 값 표시
for idx, bar in enumerate(bars):
    h = bar.get_height()

    ax.text(
        bar.get_x() + bar.get_width()/2,
        h + 0.002,
        f"{h:.2%}",
        ha='center',
        fontsize=9
    )

# 그래프 스타일
ax.set_title(
    f"{selected_mbti} 비율이 가장 높은 국가 TOP 10",
    fontsize=18
)

ax.set_xlabel("국가")
ax.set_ylabel("비율")

plt.xticks(rotation=45)
plt.tight_layout()

# 출력
st.pyplot(fig)

# 1위 국가 표시
top_country = top10.iloc[0]['Country']
top_value = top10.iloc[0][selected_mbti]

st.success(
    f"🏆 {selected_mbti} 비율 1위 국가는 "
    f"'{top_country}' ({top_value:.2%}) 입니다."
)

# 순위 테이블
st.subheader("📋 순위표")

ranking_df = pd.DataFrame({
    "순위": range(1, 11),
    "국가": top10['Country'].values,
    "비율": [f"{v:.2%}" for v in top10[selected_mbti].values]
})

st.dataframe(ranking_df, use_container_width=True)
