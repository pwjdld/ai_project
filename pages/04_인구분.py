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
    "population.csv 파일을 업로드하세요",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    # 첫 번째 컬럼(행정구명) 찾기
    region_col = df.columns[0]

    age_columns = [
        '0~9세',
        '10~19세',
        '20~29세',
        '30~39세',
        '40~49세',
        '50~59세',
        '60~69세',
        '70~79세',
        '80~89세',
        '90~99세',
        '100세 이상'
    ]

    regions = df[region_col].unique()

    selected_region = st.selectbox(
        "행정구 선택",
        regions
    )

    row = df[df[region_col] == selected_region].iloc[0]

    population = [row[col] for col in age_columns]

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=age_columns,
            y=population,
            mode='lines+markers',
            line=dict(
                color='skyblue',
                width=4
            ),
            marker=dict(
                size=8,
                color='skyblue'
            ),
            name='인구수'
        )
    )

    fig.update_layout(
        title=f"{selected_region} 연령별 인구 현황",
        plot_bgcolor="#f2f2f2",
        paper_bgcolor="white",
        height=600,
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

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("선택한 지역 데이터")

    result_df = pd.DataFrame({
        "연령대": age_columns,
        "인구수": population
    })

    st.dataframe(
        result_df,
        use_container_width=True
    )

else:
    st.info("population.csv 파일을 업로드해주세요.")
