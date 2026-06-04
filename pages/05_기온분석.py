import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="서울 기온 분석",
    layout="wide"
)

st.title("🌡️ 서울 기온 분석")

# -------------------
# 데이터 불러오기
# -------------------

try:
    df = pd.read_csv("seoul.csv", encoding="cp949")
except:
    try:
        df = pd.read_csv("seoul.csv", encoding="utf-8")
    except:
        df = pd.read_csv("seoul.csv", encoding="utf-8-sig")

# 컬럼명 공백 제거
df.columns = df.columns.str.strip()

# -------------------
# 날짜 변환
# -------------------

df["날짜"] = pd.to_datetime(
    df["날짜"],
    errors="coerce"
)

# 날짜 변환 실패 행 제거
df = df.dropna(subset=["날짜"])

# 기온 데이터 숫자 변환
df["최고기온(℃)"] = pd.to_numeric(
    df["최고기온(℃)"],
    errors="coerce"
)

df["최저기온(℃)"] = pd.to_numeric(
    df["최저기온(℃)"],
    errors="coerce"
)

df = df.dropna(
    subset=["최고기온(℃)", "최저기온(℃)"]
)

# 날짜 정렬
df = df.sort_values("날짜")

# -------------------
# 날짜 선택
# -------------------

selected_date = st.date_input(
    "날짜를 선택하세요",
    value=df["날짜"].max().date(),
    min_value=df["날짜"].min().date(),
    max_value=df["날짜"].max().date()
)

selected_date = pd.Timestamp(selected_date)

# 선택 날짜 확인
if selected_date not in df["날짜"].values:

    nearest_idx = (
        df["날짜"] - selected_date
    ).abs().idxmin()

    selected_row = df.loc[nearest_idx]
    selected_date = selected_row["날짜"]

    st.warning(
        f"선택 날짜 데이터가 없어 가장 가까운 날짜({selected_date.date()})를 표시합니다."
    )

# 선택 연도
selected_year = selected_date.year

year_df = df[
    df["날짜"].dt.year == selected_year
]

selected_row = year_df[
    year_df["날짜"] == selected_date
]

# -------------------
# 정보 표시
# -------------------

st.subheader(f"📅 {selected_year}년 기온 변화")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "최고기온",
        f"{selected_row['최고기온(℃)'].iloc[0]:.1f}℃"
    )

with col2:
    st.metric(
        "최저기온",
        f"{selected_row['최저기온(℃)'].iloc[0]:.1f}℃"
    )

# -------------------
# 그래프
# -------------------

fig = go.Figure()

# 최고기온 (초록색)
fig.add_trace(
    go.Scatter(
        x=year_df["날짜"],
        y=year_df["최고기온(℃)"],
        mode="lines",
        name="최고기온",
        line=dict(
            color="green",
            width=3
        )
    )
)

# 최저기온 (연한 하늘색)
fig.add_trace(
    go.Scatter(
        x=year_df["날짜"],
        y=year_df["최저기온(℃)"],
        mode="lines",
        name="최저기온",
        line=dict(
            color="lightskyblue",
            width=3
        )
    )
)

# 선택 날짜 최고기온
fig.add_trace(
    go.Scatter(
        x=[selected_date],
        y=[selected_row["최고기온(℃)"].iloc[0]],
        mode="markers",
        name="선택일 최고기온",
        marker=dict(size=12)
    )
)

# 선택 날짜 최저기온
fig.add_trace(
    go.Scatter(
        x=[selected_date],
        y=[selected_row["최저기온(℃)"].iloc[0]],
        mode="markers",
        name="선택일 최저기온",
        marker=dict(size=12)
    )
)

fig.update_layout(
    height=650,
    hovermode="x unified",
    template="plotly_white",
    xaxis_title="날짜",
    yaxis_title="기온(℃)",
    legend_title="범례"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
