import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="세계 행복지수 순위 변화",
    layout="wide"
)

st.title("🌎 세계 행복지수 순위 변화")
st.markdown("국가를 선택하면 연도별 행복 순위를 확인할 수 있습니다.")

# -----------------------------
# 데이터 불러오기
# -----------------------------
years = [2015, 2016, 2017, 2018, 2019]

all_data = []

for year in years:
    df = pd.read_csv(f"{year}.csv")

    # 연도별 컬럼명 통일
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
        temp.columns = ["Country", "Rank"]
        temp["Year"] = year
        all_data.append(temp)

data = pd.concat(all_data, ignore_index=True)

# -----------------------------
# 국가 선택
# -----------------------------
countries = sorted(data["Country"].unique())

selected_country = st.selectbox(
    "국가 선택",
    countries
)

country_data = data[data["Country"] == selected_country]
country_data = country_data.sort_values("Year")

# -----------------------------
# 그래프
# -----------------------------
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
            size=10,
            color="skyblue"
        ),
        name="행복 순위"
    )
)

fig.update_layout(
    title=f"{selected_country} 행복 순위 변화",
    plot_bgcolor="#f2f2f2",
    paper_bgcolor="#f2f2f2",
    xaxis_title="연도",
    yaxis_title="순위",
    height=600,
    font=dict(size=16)
)

# 1위가 위로 오도록 반전
fig.update_yaxes(autorange="reversed")

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# 데이터 표
# -----------------------------
st.subheader("연도별 순위")

st.dataframe(
    country_data[["Year", "Rank"]],
    use_container_width=True
)
