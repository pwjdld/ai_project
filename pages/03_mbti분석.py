# app.py

```python
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 페이지 설정
st.set_page_config(
    page_title="Countries MBTI Dashboard",
    layout="wide"
)

st.title("🌍 국가별 MBTI 비율 분석")
st.markdown("국가를 선택하면 MBTI 16가지 유형 비율을 시각화합니다.")

# 데이터 불러오기
@st.cache_data

def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df


df = load_data()

# 국가 선택
country_list = sorted(df['Country'].unique())
selected_country = st.selectbox(
    "국가를 선택하세요",
    country_list
)

# 선택 국가 데이터
country_data = df[df['Country'] == selected_country].iloc[0]

# MBTI 컬럼
mbti_cols = [
    'INFJ', 'ISFJ', 'INTP', 'ISFP',
    'ENTP', 'ISTP', 'INTJ', 'ESTP',
    'ENFJ', 'ESFJ', 'INFP', 'ESFP',
    'ENFP', 'ESTJ', 'ISTJ', 'ENTJ'
]

# 데이터 정리
mbti_values = country_data[mbti_cols].astype(float)
mbti_sorted = mbti_values.sort_values(ascending=False)

# 색상 설정
max_index = mbti_sorted.index[0]

colors = []
green_levels = np.linspace(0.85, 0.35, len(mbti_sorted)-1)

green_idx = 0
for mbti in mbti_sorted.index:
    if mbti == max_index:
        colors.append('blue')
    else:
        colors.append((0.0, green_levels[green_idx], 0.0))
        green_idx += 1

# 그래프 생성
fig, ax = plt.subplots(figsize=(12, 6))

bars = ax.bar(
    mbti_sorted.index,
    mbti_sorted.values,
    color=colors
)

# 값 표시
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        height + 0.002,
        f'{height:.2%}',
        ha='center',
        fontsize=9
    )

# 그래프 스타일
ax.set_title(f'{selected_country} MBTI 비율', fontsize=18)
ax.set_xlabel('MBTI 유형', fontsize=12)
ax.set_ylabel('비율', fontsize=12)
ax.set_ylim(0, mbti_sorted.max() + 0.03)

plt.xticks(rotation=45)
plt.tight_layout()

# 출력
st.pyplot(fig)

# 최고 MBTI 표시
st.subheader('🏆 가장 높은 MBTI 유형')

best_mbti = mbti_sorted.index[0]
best_value = mbti_sorted.iloc[0]

st.success(f'{selected_country}의 가장 높은 MBTI는 **{best_mbti}** ({best_value:.2%}) 입니다.')

# 데이터 테이블
st.subheader('📋 MBTI 데이터 표')

result_df = pd.DataFrame({
    'MBTI': mbti_sorted.index,
    '비율': [f'{v:.2%}' for v in mbti_sorted.values]
})

st.dataframe(result_df, use_container_width=True)
```

---

# requirements.txt

```txt
streamlit
pandas
matplotlib
numpy
```

---

# 스트림릿 클라우드 업로드 방법

1. GitHub 저장소 생성

2. 아래 파일 업로드

   * app.py
   * requirements.txt
   * countriesMBTI_16types.csv

3. Streamlit Cloud 접속

4. GitHub 저장소 연결

5. app.py 선택 후 Deploy
