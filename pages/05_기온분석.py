import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

st.title("🌡️ 서울 기온 분석")

# 데이터 불러오기
df = pd.read_csv("seoul.csv", encoding="cp949")

# 날짜 변환
df["날짜"] = pd.to_datetime(df["날짜"])

# 결측 제거
df = df.dropna(subset=["최고기온(℃)", "최저기온(℃)"])

# 날짜 선택
selected_date = st.date_input(
    "날짜를 선택하세요",
    value=df["날짜"].max().date(),
    min_value=df["날짜"].min().date(),
    max_value=df["날짜"].max().date()
)

selected_date = pd.to_datetime(selected_date)

# 선택한 날짜가 존재하는지 확인
if selected_date not in df["날짜"].values:
    st.warning("선택한 날짜의 데이터가 없습니다.")
    st.stop()

# 선택한 날짜의 연도 추출
selected_year = selected_date.year

year_df = df[df["날짜"].dt.year == selected_year]

# 선택한 날짜 데이터
selected_row = year_df[year_df["날짜"] == selected_date]

st.subheader(f"📅 {selected_year}년 기온 변화")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "최고기온",
        f"{selected_row['최고기온(℃)'].iloc[0]:.1f} ℃"
    )

with col2:
    st.metric(
        "최저기온",
        f"{selected_row['최저기온(℃)'].iloc[0]:.1f} ℃"
    )

# 그래프 생성
fig = go.Figure()

# 최고기온 (초록색)
fig.add_trace(
    go.Scatter(
        x=year_df["날짜"],
        y=year_df["최고기온(℃)"],
        mode="lines",
        name="최고기온",
        line=dict(color="green", width=3)
    )
)

# 최저기온 (연한 하늘색)
fig.add_trace(
    go.Scatter(
        x=year_df["날짜"],
        y=year_df["최저기온(℃)"],
        mode="lines",
        name="최저기온",
        line=dict(color="lightskyblue", width=3)
    )
)

# 선택 날짜 강조
fig.add_trace(
    go.Scatter(
        x=[selected_date],
        y=[selected_row["최고기온(℃)"].iloc[0]],
        mode="markers",
        marker=dict(size=12),
        name="선택일 최고기온"
    )
)

fig.add_trace(
    go.Scatter(
        x=[selected_date],
        y=[selected_row["최저기온(℃)"].iloc[0]],
        mode="markers",
        marker=dict(size=12),
        name="선택일 최저기온"
    )
)

fig.update_layout(
    height=650,
    xaxis_title="날짜",
    yaxis_title="기온 (℃)",
    hovermode="x unified",
    legend_title="범례",
    template="plotly_white"
)

st.plotly_chart(fig, use_container_width=True)
