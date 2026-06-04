import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np

st.set_page_config(
    page_title="서울 기온 분석 및 미래 예측",
    layout="wide"
)

st.title("🌡️ 서울 기온 분석 및 미래 예측")

# -----------------------
# 데이터 불러오기
# -----------------------

try:
    df = pd.read_csv("seoul.csv", encoding="cp949")
except:
    try:
        df = pd.read_csv("seoul.csv", encoding="utf-8")
    except:
        df = pd.read_csv("seoul.csv", encoding="utf-8-sig")

df.columns = df.columns.str.strip()

# 날짜 변환
df["날짜"] = pd.to_datetime(
    df["날짜"],
    errors="coerce",
    format="mixed"
)

df = df.dropna(subset=["날짜"])

# 기온 숫자 변환
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

# -----------------------
# 연도 생성
# -----------------------

df["연도"] = df["날짜"].dt.year

yearly = (
    df.groupby("연도")
    .agg({
        "최고기온(℃)": "max",
        "최저기온(℃)": "min"
    })
    .reset_index()
)

# -----------------------
# 예측모델 생성
# -----------------------

X = yearly[["연도"]]

max_model = LinearRegression()
max_model.fit(X, yearly["최고기온(℃)"])

min_model = LinearRegression()
min_model.fit(X, yearly["최저기온(℃)"])

# -----------------------
# 연도 선택
# -----------------------

min_year = int(yearly["연도"].min())
max_year = int(yearly["연도"].max())

selected_year = st.slider(
    "연도를 선택하세요",
    min_value=min_year,
    max_value=2100,
    value=max_year
)

# -----------------------
# 실제 데이터 또는 예측
# -----------------------

if selected_year <= max_year:

    row = yearly[yearly["연도"] == selected_year]

    max_temp = row["최고기온(℃)"].iloc[0]
    min_temp = row["최저기온(℃)"].iloc[0]

    title = f"{selected_year}년 실제 기온"

else:

    max_temp = max_model.predict([[selected_year]])[0]
    min_temp = min_model.predict([[selected_year]])[0]

    title = f"{selected_year}년 예측 기온"

# -----------------------
# 결과 표시
# -----------------------

st.subheader(title)

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "최고기온",
        f"{max_temp:.1f}℃"
    )

with col2:
    st.metric(
        "최저기온",
        f"{min_temp:.1f}℃"
    )

# -----------------------
# 미래 예측 데이터 생성
# -----------------------

future_years = np.arange(
    min_year,
    210
