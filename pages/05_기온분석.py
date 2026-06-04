# pages/05_기온분석.py

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from sklearn.linear_model import LinearRegression
from pathlib import Path

st.set_page_config(
page_title="서울 기온 분석",
layout="wide"
)

st.title("🌡️ 서울 기온 분석 및 미래 예측")

# -------------------------

# CSV 불러오기

# -------------------------

BASE_DIR = Path(**file**).resolve().parent.parent
csv_path = BASE_DIR / "seoul.csv"

try:
df = pd.read_csv(csv_path, encoding="cp949")
except:
try:
df = pd.read_csv(csv_path, encoding="utf-8")
except:
df = pd.read_csv(csv_path, encoding="utf-8-sig")

# 컬럼명 공백 제거

df.columns = df.columns.str.strip()

# -------------------------

# 날짜 변환

# -------------------------

df["날짜"] = pd.to_datetime(
df["날짜"],
errors="coerce"
)

df = df.dropna(subset=["날짜"])

# 기온 숫자형 변환

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

# -------------------------

# 연도 생성

# -------------------------

df["연도"] = df["날짜"].dt.year

yearly = (
df.groupby("연도")
.agg(
{
"최고기온(℃)": "max",
"최저기온(℃)": "min"
}
)
.reset_index()
)

# -------------------------

# 선형회귀 모델

# -------------------------

X = yearly[["연도"]]

max_model = LinearRegression()
max_model.fit(X, yearly["최고기온(℃)"])

min_model = LinearRegression()
min_model.fit(X, yearly["최저기온(℃)"])

# -------------------------

# 연도 선택

# -------------------------

min_year = int(yearly["연도"].min())
max_year = int(yearly["연도"].max())

selected_year = st.slider(
"연도 선택",
min_value=min_year,
max_value=2100,
value=max_year
)

# -------------------------

# 실제 데이터

# -------------------------

if selected_year <= max_year:

```
row = yearly[
    yearly["연도"] == selected_year
]

max_temp = row["최고기온(℃)"].iloc[0]
min_temp = row["최저기온(℃)"].iloc[0]

st.subheader(f"📊 {selected_year}년 실제 기온")
```

# -------------------------

# 미래 예측

# -------------------------

else:

```
max_temp = max_model.predict(
    [[selected_year]]
)[0]

min_temp = min_model.predict(
    [[selected_year]]
)[0]

st.subheader(f"🔮 {selected_year}년 예측 기온")
```

# -------------------------

# 메트릭

# -------------------------

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

# -------------------------

# 미래 예측 데이터 생성

# -------------------------

future_years = np.arange(
min_year,
2101
)

pred_max = max_model.predict(
future_years.reshape(-1, 1)
)

pred_min = min_model.predict(
future_years.reshape(-1, 1)
)

# -------------------------

# 그래프

# -------------------------

fig = go.Figure()

fig.add_trace(
go.Scatter(
x=future_years,
y=pred_max,
mode="lines",
name="예측 최고기온",
line=dict(
color="green",
width=3
)
)
)

fig.add_trace(
go.Scatter(
x=future_years,
y=pred_min,
mode="lines",
name="예측 최저기온",
line=dict(
color="lightskyblue",
width=3
)
)
)

fig.add_vline(
x=max_year,
line_dash="dash"
)

fig.update_layout(
height=650,
template="plotly_white",
legend_title="범례",
xaxis_title="연도",
yaxis_title="기온(℃)"
)

st.plotly_chart(
fig,
use_container_width=True
)
