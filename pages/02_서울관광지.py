# app.py

import streamlit as st
import folium
from folium.plugins import MiniMap
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
        "fun": """
🏯 조선 시대 궁궐을 직접 걸어보며 한국 전통문화를 느낄 수 있어.
👘 한복을 입고 사진 찍는 외국인 관광객들이 정말 많아.
📸 근정전, 경회루 같은 인기 포토존에서 인생샷 찍기 좋아.
☕ 주변 서촌 카페거리까지 함께 구경하면 하루 코스로 딱이야.
"""
    },
    {
        "name": "남산서울타워",
        "lat": 37.5512,
        "lon": 126.9882,
        "station": "명동역 (4호선)",
        "fun": """
🌃 서울 야경을 한눈에 볼 수 있는 대표 전망대야.
🔒 사랑의 자물쇠 명소로 커플 관광객들에게 특히 인기 많아.
🚠 케이블카를 타고 올라가는 재미도 있어.
📷 밤에 가면 서울 전체가 반짝이는 모습이 정말 예뻐.
"""
    },
    {
        "name": "명동",
        "lat": 37.5637,
        "lon": 126.9827,
        "station": "명동역 (4호선)",
        "fun": """
🛍️ 화장품 쇼핑과 패션 쇼핑으로 유명한 거리야.
🍢 길거리 음식 먹방 코스로 외국인들이 정말 좋아해.
🎵 밤이 되면 거리 분위기가 더 활기차고 재밌어져.
☕ 다양한 카페와 디저트 맛집도 많아 쉬기 좋아.
"""
    },
    {
        "name": "홍대거리",
        "lat": 37.5563,
        "lon": 126.9220,
        "station": "홍대입구역 (2호선)",
        "fun": """
🎸 버스킹 공연과 스트리트 문화가 유명한 핫플레이스야.
☕ 감성 카페와 개성 있는 소품샵이 정말 많아.
🍜 맛집 탐방과 야간 거리 구경이 특히 재밌어.
🕺 밤에는 클럽과 공연장 분위기도 활발해져.
"""
    },
    {
        "name": "롯데월드타워",
        "lat": 37.5131,
        "lon": 127.1025,
        "station": "잠실역 (2호선)",
        "fun": """
🏙️ 서울 스카이를 통해 초고층 전망을 즐길 수 있어.
🛍️ 대형 쇼핑몰과 아쿠아리움이 함께 있어서 하루 종일 놀기 좋아.
🎢 근처 롯데월드 놀이공원도 함께 즐길 수 있어.
📸 석촌호수 주변 산책 코스도 정말 인기 많아.
"""
    },
    {
        "name": "북촌한옥마을",
        "lat": 37.5826,
        "lon": 126.9830,
        "station": "안국역 (3호선)",
        "fun": """
🏡 전통 한옥 골목길 감성이 정말 아름다운 곳이야.
📸 한국 전통 분위기 사진 찍기에 최고의 장소로 유명해.
☕ 한옥 카페와 공방 체험도 즐길 수 있어.
🚶 삼청동 거리까지 함께 산책하면 더 좋아.
"""
    },
    {
        "name": "동대문디자인플라자",
        "lat": 37.5665,
        "lon": 127.0092,
        "station": "동대문역사문화공원역",
        "fun": """
✨ 미래적인 건축 디자인으로 유명한 서울 랜드마크야.
🖼️ 다양한 전시회와 디자인 행사가 자주 열려.
🌙 밤에는 LED 장미정원 야경이 정말 예뻐.
🛍️ 근처 동대문 쇼핑타운까지 함께 즐길 수 있어.
"""
    },
    {
        "name": "한강공원",
        "lat": 37.5207,
        "lon": 126.9395,
        "station": "여의나루역 (5호선)",
        "fun": """
🚴 자전거를 타며 한강 바람을 즐기기 좋아.
🍗 치킨과 라면 먹으며 피크닉하는 문화가 유명해.
🌅 저녁 노을과 야경이 정말 아름다워.
🛥️ 유람선과 수상 레저 체험도 가능해.
"""
    },
    {
        "name": "코엑스",
        "lat": 37.5126,
        "lon": 127.0582,
        "station": "삼성역 (2호선)",
        "fun": """
📚 별마당도서관이 SNS 포토존으로 엄청 유명해.
🛍️ 쇼핑몰, 영화관, 맛집이 한곳에 모여 있어.
🐠 코엑스 아쿠아리움도 가족 관광객들에게 인기야.
☕ 실내 공간이라 날씨 상관없이 편하게 놀 수 있어.
"""
    },
    {
        "name": "인사동",
        "lat": 37.5740,
        "lon": 126.9850,
        "station": "안국역 (3호선)",
        "fun": """
🎨 전통 공예품과 한국 기념품 쇼핑으로 유명해.
🍡 길거리 전통 간식 먹는 재미가 있어.
☕ 전통 찻집과 감성 카페가 정말 많아.
🖌️ 한국 전통문화를 느끼기 좋은 관광 코스야.
"""
    }
]

# 컬러 지도 + 한국어 지도 타일 사용
m = folium.Map(
    location=[37.5665, 126.9780],
    zoom_start=11,
    tiles="OpenStreetMap"
)

# 미니맵 추가
MiniMap().add_to(m)

# 마커 추가
for place in places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        tooltip=f"🚇 가까운 역: {place['station']}",
        popup=place["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 지도 출력 (기존보다 약 60% 크기)
map_html = m._repr_html_()

st.markdown("### 🗺️ 서울 관광 지도")

html(map_html, height=360)

st.markdown("---")

# 관광지 선택
st.header("📍 관광지 상세 정보")

selected_place = st.selectbox(
    "관광지를 선택해봐 😊",
    [place["name"] for place in places]
)

# 선택된 관광지 정보 출력
for place in places:
    if place["name"] == selected_place:
        st.subheader(f"🌟 {place['name']}")

        st.write(f"🚇 가장 가까운 지하철역: {place['station']}")

        st.markdown("### 🎈 놀거리 & 추천 포인트")
        st.write(place["fun"])

        # 추가 좌표 정보
        st.markdown("### 📌 위치 정보")
        st.write(f"위도: {place['lat']}")
        st.write(f"경도: {place['lon']}")

        break
