# app.py

import streamlit as st
import folium
from streamlit.components.v1 import html

st.set_page_config(
    page_title="서울 관광지 TOP10 🗺️",
    page_icon="📍",
    layout="wide"
)

st.title("🌆 외국인들이 좋아하는 서울 관광지 TOP10")
st.write("지도를 움직이며 서울의 인기 관광지를 구경해봐! 😆")

# 관광지 데이터
places = [
    {
        "name": "경복궁",
        "lat": 37.5796,
        "lon": 126.9770,
        "station": "경복궁역 (3호선)",
        "fun": "한복 체험과 궁궐 사진 찍기로 유명해 👘"
    },
    {
        "name": "남산서울타워",
        "lat": 37.5512,
        "lon": 126.9882,
        "station": "명동역 (4호선)",
        "fun": "야경 맛집! 사랑의 자물쇠도 유명해 🔒"
    },
    {
        "name": "명동",
        "lat": 37.5637,
        "lon": 126.9827,
        "station": "명동역 (4호선)",
        "fun": "길거리 음식과 쇼핑 천국 🍢🛍️"
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9220,
        "station": "홍대입구역 (2호선)",
        "fun": "버스킹, 카페, 맛집으로 핫한 곳 🎸"
    },
    {
        "name": "롯데월드타워",
        "lat": 37.5131,
        "lon": 127.1025,
        "station": "잠실역 (2호선)",
        "fun": "전망대와 쇼핑몰이 엄청 커 😲"
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.5826,
        "lon": 126.9830,
        "station": "안국역 (3호선)",
        "fun": "전통 한옥 감성 사진 찍기 최고 📸"
    },
    {
        "name": "동대문디자인플라자",
        "lat": 37.5665,
        "lon": 127.0092,
        "station": "동대문역사문화공원역",
        "fun": "야경과 전시회가 인기야 ✨"
    },
    {
        "name": "한강공원",
        "lat": 37.5207,
        "lon": 126.9395,
        "station": "여의나루역 (5호선)",
        "fun": "치킨 먹으며 자전거 타기 최고 🚴🍗"
    },
    {
        "name": "코엑스",
        "lat": 37.5126,
        "lon": 127.0582,
        "station": "삼성역 (2호선)",
        "fun": "별마당도서관이 진짜 예뻐 📚"
    },
    {
        "name": "인사동",
        "lat": 37.5740,
        "lon": 126.9850,
        "station": "안국역 (3호선)",
        "fun": "전통 기념품과 길거리 간식이 많아 🍡"
    }
]

# 지도 생성
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11
)

# 마커 추가
for place in places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        tooltip=f"🚇 가까운 역: {place['station']}",
        popup=place["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 지도 출력
map_html = m._repr_html_()
html(map_html, height=600)

st.markdown("---")
st.header("📍 관광지 & 가까운 지하철역 정보")

for idx, place in enumerate(places, start=1):
    st.subheader(f"{idx}. {place['name']}")

    st.write(f"🚇 가까운 역: {place['station']}")
    st.write(f"🎈 놀거리: {place['fun']}")

    st.markdown("---")
