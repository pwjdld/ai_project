# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------
# 페이지 설정
# -----------------------------------
st.set_page_config(
    page_title="MBTI World Dashboard",
    layout="wide"
)

st.title("🌍 국가별 MBTI 분석 대시보드")

# -----------------------------------
# 데이터 불러오기
# -----------------------------------
@st.cache_data
def load_data():
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

# MBTI 컬럼
mbti_cols = [
    'INFJ', 'ISFJ', 'INTP', 'ISFP',
    'ENTP', 'ISTP', 'INTJ', 'ESTP',
    'ENFJ', 'ESFJ', 'INFP', 'ESFP',
    'ENFP', 'ESTJ', 'ISTJ', 'ENTJ'
]

# -----------------------------------
# 탭 생성
# -----------------------------------
tab1, tab2 = st.tabs([
    "📊 국가별 MBTI 분석",
    "🏆 MBTI 유형별 TOP10 국가"
])

# =========================================================
# TAB 1 : 국가별 MBTI 분석
# =========================================================
with tab1:

    st.header("📊 국가별 MBTI 비율")

    # 국가 선택
    country = st.selectbox(
        "국가 선택",
        sorted(df["Country"].unique())
    )

    # 데이터 추출
    selected = df[df["Country"] == country].iloc[0]

    values = selected[mbti_cols].astype(float)

    # 내림차순 정렬
    values = values.sort_values(ascending=False)

    # 색상 설정
    colors = []

    green_gradient = np.linspace(
        0.85,
        0.35,
        len(values)-1
    )

    idx = 0

    for i, mbti in enumerate(values.index):

        # 1등 → 파랑
        if i == 0:
            colors.append("blue")

        # 나머지 → 초록 그라데이션
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
    ax.set_title(
        f"{country} MBTI 비율",
        fontsize=18
    )

    ax.set_xlabel("MBTI 유형")
    ax.set_ylabel("비율")

    plt.xticks(rotation=45)

    plt.tight_layout()

    st.pyplot(fig)

    # 최고 MBTI 표시
    top_mbti = values.index[0]
    top_value = values.iloc[0]

    st.success(
        f"🏆 {country}의 가장 높은 MBTI는 "
        f"'{top_mbti}' ({top_value:.2%}) 입니다."
    )

    # 테이블
    st.subheader("📋 MBTI 데이터")

    table_df = pd.DataFrame({
        "MBTI": values.index,
        "비율": [f"{v:.2%}" for v in values.values]
    })

    st.dataframe(
        table_df,
        use_container_width=True
    )

# =========================================================
# TAB 2 : MBTI 유형별 TOP10 국가
# =========================================================
with tab2:

    st.header("🏆 MBTI 유형별 상위 10개 국가")

    # MBTI 선택
    selected_mbti = st.selectbox(
        "MBTI 유형 선택",
        mbti_cols
    )

    # TOP10 데이터
    top10 = df[['Country', selected_mbti]] \
        .sort_values(
            by=selected_mbti,
            ascending=False
        ) \
        .head(10)

    # 색상 설정
    colors = ['blue']

    green_gradient = np.linspace(
        0.85,
        0.35,
        9
    )

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
    ax.set_title(
        f"{selected_mbti} 비율 TOP 10 국가",
        fontsize=18
    )

    ax.set_xlabel("국가")
    ax.set_ylabel("비율")

    plt.xticks(rotation=45)

    plt.tight_layout()

    st.pyplot(fig)

    # 1위 국가
    top_country = top10.iloc[0]['Country']
    top_value = top10.iloc[0][selected_mbti]

    st.success(
        f"🏆 {selected_mbti} 비율 1위 국가는 "
        f"'{top_country}' ({top_value:.2%}) 입니다."
    )

    # 순위표
    st.subheader("📋 순위표")

    ranking_df = pd.DataFrame({
        "순위": range(1, 11),
        "국가": top10['Country'].values,
        "비율": [
            f"{v:.2%}"
            for v in top10[selected_mbti].values
        ]
    })

    st.dataframe(
        ranking_df,
        use_container_width=True
    )
