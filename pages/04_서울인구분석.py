import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="서울 연령별 인구 분석",
    page_icon="📊",
    layout="wide"
)

st.title("📊 서울 연령별 인구 분석")

uploaded_file = st.file_uploader(
    "population.csv 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    # 서울시 인구 CSV는 CP949(EUC-KR)
    df = pd.read_csv(
        uploaded_file,
        encoding="cp949"
    )

    # 컬럼 공백 제거
    df.columns = df.columns.str.strip()

    # 행정구역 컬럼
    region_col = "행정구역"

    # 연령 컬럼
    age_columns = [
        "0~9세",
        "10~19세",
        "20~29세",
        "30~39세",
        "40~49세",
        "50~59세",
        "60~69세",
        "70~79세",
        "80~89세",
        "90~99세",
        "2026년04월_거주자_100세 이상"
    ]

    # 행정구 선택
    selected_region = st.selectbox(
        "행정구 선택",
        df[region_col]
    )

    row = df[df[region_col] == selected_region].iloc[0]

    populations = []

    for col in age_columns:
        value = str(row[col]).replace(",", "")
        populations.append(int(value))

    # 보기 좋게 이름 변경
    age_labels = [
        "0~9세",
        "10~19세",
        "20~29세",
        "30~39세",
        "40~49세",
        "50~59세",
        "60~69세",
        "70~79세",
        "80~89세",
        "90~99세",
        "100세 이상"
    ]

    # 그래프
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=age_labels,
            y=populations,
            mode="lines+markers",
            line=dict(
                color="skyblue",
                width=4
            ),
            marker=dict(
                color="skyblue",
                size=8
            )
        )
    )

    fig.update_layout(
        title=f"{selected_region} 연령별 인구",
        height=600,
        plot_bgcolor="#f2f2f2",
        paper_bgcolor="white",
        xaxis_title="나이",
        yaxis_title="인구수",
        hovermode="x unified"
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="white"
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("연령별 인구 데이터")

    result_df = pd.DataFrame({
        "연령대": age_labels,
        "인구수": populations
    })

    st.dataframe(
        result_df,
        use_container_width=True
    )

else:
    st.info("population.csv 파일을 업로드하세요.")
