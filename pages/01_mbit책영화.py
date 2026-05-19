import streamlit as st

st.set_page_config(
    page_title="MBTI 책 & 영화 추천 📚🎬",
    page_icon="✨",
    layout="centered"
)

# MBTI 추천 데이터
mbti_data = {
    "INTJ": {
        "books": [
            {
                "title": "📘 1984",
                "author": "조지 오웰",
                "year": "1949",
                "desc": "깊게 생각하는 INTJ에게 딱 맞는 디스토피아 명작!"
            },
            {
                "title": "🚀 프로젝트 헤일메리",
                "author": "앤디 위어",
                "year": "2021",
                "desc": "과학과 전략 좋아하는 INTJ 취향 저격!"
            }
        ],
        "movies": [
            {
                "title": "🎬 시민 케인",
                "year": "1941",
                "desc": "생각할 거리 많은 미국 영화의 전설!"
            },
            {
                "title": "🕵️ 대부",
                "year": "1972",
                "desc": "전략과 권력 이야기를 좋아한다면 추천!"
            }
        ]
    },

    "INFP": {
        "books": [
            {
                "title": "🌙 어린 왕자",
                "author": "생텍쥐페리",
                "year": "1943",
                "desc": "감성 가득한 INFP 마음을 울리는 책 💖"
            },
            {
                "title": "🪐 아몬드",
                "author": "손원평",
                "year": "2017",
                "desc": "따뜻하면서도 깊은 감정을 느낄 수 있어!"
            }
        ],
        "movies": [
            {
                "title": "🎥 로마의 휴일",
                "year": "1953",
                "desc": "감성 폭발하는 클래식 로맨스 ✨"
            },
            {
                "title": "🎭 사운드 오브 뮤직",
                "year": "1965",
                "desc": "따뜻하고 힐링되는 분위기가 매력적!"
            }
        ]
    },

    "ENFP": {
        "books": [
            {
                "title": "⚓ 노인과 바다",
                "author": "어니스트 헤밍웨이",
                "year": "1952",
                "desc": "도전 정신 넘치는 이야기!"
            },
            {
                "title": "🌈 죽고 싶지만 떡볶이는 먹고 싶어",
                "author": "백세희",
                "year": "2018",
                "desc": "솔직한 감정 이야기에 공감하게 될 거야!"
            }
        ],
        "movies": [
            {
                "title": "🎸 백 투 더 퓨처",
                "year": "1985",
                "desc": "모험과 유쾌함 가득한 영화!"
            },
            {
                "title": "🚲 이티",
                "year": "1982",
                "desc": "상상력 넘치는 감동 SF 영화 👽"
            }
        ]
    },

    "ISTJ": {
        "books": [
            {
                "title": "⚖️ 죄와 벌",
                "author": "도스토예프스키",
                "year": "1866",
                "desc": "진지하고 논리적인 ISTJ에게 추천!"
            },
            {
                "title": "📚 불편한 편의점",
                "author": "김호연",
                "year": "2021",
                "desc": "따뜻한 현실 이야기가 매력적 😊"
            }
        ],
        "movies": [
            {
                "title": "🚢 타이타닉",
                "year": "1997",
                "desc": "명작은 역시 명작!"
            },
            {
                "title": "🎩 카사블랑카",
                "year": "1942",
                "desc": "클래식 영화 입문으로 최고!"
            }
        ]
    },

    "ENTP": {
        "books": [
            {
                "title": "🧠 멋진 신세계",
                "author": "올더스 헉슬리",
                "year": "1932",
                "desc": "아이디어 넘치는 ENTP에게 딱!"
            },
            {
                "title": "🔥 지적 대화를 위한 넓고 얕은 지식",
                "author": "채사장",
                "year": "2014",
                "desc": "다양한 분야를 재밌게 배울 수 있어!"
            }
        ],
        "movies": [
            {
                "title": "🚀 스타워즈",
                "year": "1977",
                "desc": "상상력 폭발 SF 전설!"
            },
            {
                "title": "🕶️ 12인의 성난 사람들",
                "year": "1957",
                "desc": "토론 좋아하는 사람이라면 꼭 봐야 함!"
            }
        ]
    }
}

# 없는 MBTI용 기본 데이터
default_data = {
    "books": [
        {
            "title": "📖 데미안",
            "author": "헤르만 헤세",
            "year": "1919",
            "desc": "청소년들이 많이 사랑하는 성장 소설!"
        },
        {
            "title": "✨ 달러구트 꿈 백화점",
            "author": "이미예",
            "year": "2020",
            "desc": "상상력 가득한 힐링 판타지!"
        }
    ],
    "movies": [
        {
            "title": "🎬 오즈의 마법사",
            "year": "1939",
            "desc": "클래식 감성 최고 🌈"
        },
        {
            "title": "🧙 스타워즈",
            "year": "1977",
            "desc": "세대를 초월한 SF 명작!"
        }
    ]
}

st.title("✨ MBTI 책 & 영화 추천 ✨")

st.write("안녕 😆")
st.write("너의 MBTI에 어울리는 책과 영화를 추천해줄게!")
st.write("취향 저격일 수도 있으니까 기대해봐 👀")

mbti_list = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISTP", "ESTJ", "ESTP",
    "ISFJ", "ISFP", "ESFJ", "ESFP"
]

selected_mbti = st.selectbox(
    "🌈 MBTI 선택하기",
    mbti_list
)

if st.button("🔍 추천 받기"):
    
    data = mbti_data.get(selected_mbti, default_data)

    st.success(f"{selected_mbti} 유형 추천 시작 😎")

    st.markdown("## 📚 추천 책 2권")

    for book in data["books"]:
        st.markdown("---")
        st.subheader(book["title"])
        st.write(f"✍️ 작가: {book['author']}")
        st.write(f"📅 출간 연도: {book['year']}")
        st.write(f"💡 한줄 추천: {book['desc']}")

    st.markdown("## 🎬 추천 영화 2편")

    for movie in data["movies"]:
        st.markdown("---")
        st.subheader(movie["title"])
        st.write(f"📅 개봉 연도: {movie['year']}")
        st.write(f"🍿 추천 이유: {movie['desc']}")

    st.balloons()

st.markdown("---")
st.caption("🌟 재미로 보는 추천이니까 가볍게 즐겨줘 😆")
