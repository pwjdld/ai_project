import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from pathlib import Path

# --------------------------------------------------
# 페이지 설정
# --------------------------------------------------

st.set_page_config(
    page_title="세계 행복지수 분석",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 세계 행복지수 분석")
st.markdown("국가별 행복 순위 변화와 세계 순위를 확인해보세요.")

# --------------------------------------------------
# CSV 파일 자동 찾기
# --------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent

csv_files = {}

for year in [2015, 2016, 2017, 2018, 2019]:

    matches = list(ROOT_DIR.rglob(f"{year}.csv"))

    if matches:
        csv_files[year] = matches[0]

if len(csv_files) == 0:
    st.error("CSV 파일을 찾을 수 없습니다.")
    st.stop()

# --------------------------------------------------
# 데이터 로드
# --------------------------------------------------

all_data = []

for year, file_path in csv_files.items():

    df = pd.read_csv(file_path)

    country_col = None
    rank_col = None

    for col in df.columns:
        if "Country" in col:
            country_col = col

    for col in df.columns:
        if "Rank" in col:
            rank_col = col

    if country_col and rank_col:

        temp = df[[country_col, rank_col]].copy()

        temp.columns = [
            "Country",
            "Rank"
        ]

        temp["Year"] = year

        all_data.append(temp)

data = pd.concat(all_data, ignore_index=True)

# --------------------------------------------------
# 사이드바
# --------------------------------------------------

st.sidebar.header("설정")

selected_country = st.sidebar.selectbox(
    "국가 선택",
    sorted(data["Country"].unique())
)

selected_year = st.sidebar.selectbox(
    "연도 선택",
    sorted(data["Year"].unique())
)

# --------------------------------------------------
# 국가별 순위 변화
# --------------------------------------------------

country_data = (
    data[data["Country"] == selected_country]
    .sort_values("Year")
)

st.header(f"📈 {selected_country} 행복 순위 변화")

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=country_data["Year"],
        y=country_data["Rank"],
        mode="lines+markers",
        line=dict(
            color="skyblue",
            width=4
        ),
        marker=dict(
            color="skyblue",
            size=10
        ),
        name="행복 순위"
    )
)

fig.update_layout(
    plot_bgcolor="#f5f5f5",
    paper_bgcolor="#f5f5f5",
    xaxis_title="연도",
    yaxis_title="순위",
    height=600,
    font=dict(size=15)
)

# 1위가 위에 오도록
fig.update_yaxes(
    autorange="reversed"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------------------------
# 선택 국가 데이터
# --------------------------------------------------

st.subheader("📋 연도별 순위")

st.dataframe(
    country_data[["Year", "Rank"]],
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# 세계 순위 TOP 10 / 최하위 10
# --------------------------------------------------

st.divider()

st.header(f"🌎 {selected_year} 세계 행복 순위")

year_data = data[data["Year"] == selected_year].copy()

top10 = (
    year_data
    .sort_values("Rank")
    .head(10)
    .reset_index(drop=True)
)

top10.index = top10.index + 1

bottom10 = (
    year_data
    .sort_values("Rank", ascending=False)
    .head(10)
    .reset_index(drop=True)
)

bottom10.index = bottom10.index + 1

col1, col2 = st.columns(2)

with col1:

    st.subheader("🏆 TOP 10 국가")

    st.dataframe(
        top10[["Country", "Rank"]],
        use_container_width=True
    )

with col2:

    st.subheader("📉 최하위 10개국")

    st.dataframe(
        bottom10[["Country", "Rank"]],
        use_container_width=True
    )

# --------------------------------------------------
# 통계 정보
# --------------------------------------------------

st.divider()

st.header("📊 선택 국가 통계")

best_rank = int(country_data["Rank"].min())
worst_rank = int(country_data["Rank"].max())

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "최고 순위",
        f"{best_rank}위"
    )

with col2:
    st.metric(
        "최저 순위",
        f"{worst_rank}위"
    )
