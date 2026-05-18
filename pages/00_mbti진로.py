import streamlit as st

st.set_page_config(
    page_title="MBTI 진로 추천 🌈",
    page_icon="✨",
    layout="centered"
)

# MBTI별 진로 데이터
mbti_data = {
    "INTJ": {
        "jobs": [
            {
                "name": "🧠 데이터 분석가",
                "major": "통계학과, 컴퓨터공학과",
                "personality": "논리적이고 계획 세우는 걸 좋아하는 성격!",
                "salary": "평균 연봉 약 4,500만 원"
            },
            {
                "name": "🚀 전략 기획자",
                "major": "경영학과, 경제학과",
                "personality": "미래를 설계하고 아이디어 짜는 걸 좋아하는 타입!",
                "salary": "평균 연봉 약 5,000만 원"
            }
        ]
    },

    "INTP": {
        "jobs": [
            {
                "name": "💻 프로그래머",
                "major": "소프트웨어학과, 컴퓨터공학과",
                "personality": "혼자 깊게 생각하고 문제 푸는 걸 좋아함!",
                "salary": "평균 연봉 약 4,800만 원"
            },
            {
                "name": "🔬 연구원",
                "major": "물리학과, 화학과",
                "personality": "호기심 많고 탐구하는 걸 즐기는 성격!",
                "salary": "평균 연봉 약 4,700만 원"
            }
        ]
    },

    "ENTJ": {
        "jobs": [
            {
                "name": "📈 CEO / 경영인",
                "major": "경영학과",
                "personality": "리더십 있고 추진력이 강한 스타일!",
                "salary": "평균 연봉 약 6,000만 원 이상"
            },
            {
                "name": "⚖️ 변호사",
                "major": "법학과",
                "personality": "논리적으로 말 잘하고 책임감 강한 타입!",
                "salary": "평균 연봉 약 7,000만 원"
            }
        ]
    },

    "ENTP": {
        "jobs": [
            {
                "name": "🎤 마케터",
                "major": "광고홍보학과",
                "personality": "아이디어 넘치고 사람들과 소통 잘함!",
                "salary": "평균 연봉 약 4,300만 원"
            },
            {
                "name": "📺 콘텐츠 기획자",
                "major": "미디어학과",
                "personality": "창의적이고 트렌드에 민감한 성격!",
                "salary": "평균 연봉 약 4,000만 원"
            }
        ]
    },

    "INFJ": {
        "jobs": [
            {
                "name": "🩺 심리상담사",
                "major": "심리학과",
                "personality": "공감 능력이 뛰어나고 따뜻한 성격!",
                "salary": "평균 연봉 약 3,800만 원"
            },
            {
                "name": "✍️ 작가",
                "major": "문예창작과",
                "personality": "감수성이 풍부하고 상상력이 뛰어남!",
                "salary": "평균 연봉 약 3,500만 원"
            }
        ]
    },

    "INFP": {
        "jobs": [
            {
                "name": "🎨 일러스트레이터",
                "major": "디자인학과",
                "personality": "창의적이고 감성적인 스타일!",
                "salary": "평균 연봉 약 3,600만 원"
            },
            {
                "name": "🎬 영화 감독",
                "major": "영상학과",
                "personality": "자기만의 세계관이 뚜렷한 성격!",
                "salary": "평균 연봉 약 4,200만 원"
            }
        ]
    },

    "ENFJ": {
        "jobs": [
            {
                "name": "👩‍🏫 교사",
                "major": "교육학과",
                "personality": "사람 도와주는 걸 좋아하는 성격!",
                "salary": "평균 연봉 약 4,500만 원"
            },
            {
                "name": "🗣️ HR 담당자",
                "major": "경영학과",
                "personality": "사람들과 잘 어울리고 배려심 많음!",
                "salary": "평균 연봉 약 4,300만 원"
            }
        ]
    },

    "ENFP": {
        "jobs": [
            {
                "name": "📸 크리에이터",
                "major": "미디어학과",
                "personality": "에너지 넘치고 표현력이 좋음!",
                "salary": "평균 연봉 약 4,000만 원"
            },
            {
                "name": "🌍 여행 기획자",
                "major": "관광학과",
                "personality": "새로운 경험 좋아하고 활발함!",
                "salary": "평균 연봉 약 3,900만 원"
            }
        ]
    },

    "ISTJ": {
        "jobs": [
            {
                "name": "🏦 회계사",
                "major": "회계학과",
                "personality": "꼼꼼하고 책임감 강한 타입!",
                "salary": "평균 연봉 약 6,000만 원"
            },
            {
                "name": "👮 경찰관",
                "major": "경찰행정학과",
                "personality": "원칙을 중요하게 생각하는 성격!",
                "salary": "평균 연봉 약 4,700만 원"
            }
        ]
    },

    "ISFJ": {
        "jobs": [
            {
                "name": "💉 간호사",
                "major": "간호학과",
                "personality": "배려심 많고 성실한 스타일!",
                "salary": "평균 연봉 약 4,500만 원"
            },
            {
                "name": "🏫 사회복지사",
                "major": "사회복지학과",
                "personality": "다른 사람을 돕는 걸 좋아함!",
                "salary": "평균 연봉 약 3,500만 원"
            }
        ]
    },

    "ESTJ": {
        "jobs": [
            {
                "name": "🏢 공무원",
                "major": "행정학과",
                "personality": "체계적이고 책임감 강함!",
                "salary": "평균 연봉 약 4,800만 원"
            },
            {
                "name": "📊 프로젝트 매니저",
                "major": "경영학과",
                "personality": "리더십 있고 관리 능력이 뛰어남!",
                "salary": "평균 연봉 약 5,500만 원"
            }
        ]
    },

    "ESFJ": {
        "jobs": [
            {
                "name": "🎓 학원 강사",
                "major": "교육학과",
                "personality": "친절하고 소통을 좋아함!",
                "salary": "평균 연봉 약 4,000만 원"
            },
            {
                "name": "🏥 병원 코디네이터",
                "major": "보건행정학과",
                "personality": "사람 챙기는 걸 잘하는 타입!",
                "salary": "평균 연봉 약 3,800만 원"
            }
        ]
    },

    "ISTP": {
        "jobs": [
            {
                "name": "🔧 기계 엔지니어",
                "major": "기계공학과",
                "personality": "손으로 직접 만드는 걸 좋아함!",
                "salary": "평균 연봉 약 5,000만 원"
            },
            {
                "name": "✈️ 파일럿",
                "major": "항공운항학과",
                "personality": "침착하고 문제 해결 능력이 좋음!",
                "salary": "평균 연봉 약 7,000만 원"
            }
        ]
    },

    "ISFP": {
        "jobs": [
            {
                "name": "🎵 음악 프로듀서",
                "major": "실용음악과",
                "personality": "감각적이고 예술적인 성향!",
                "salary": "평균 연봉 약 4,200만 원"
            },
            {
                "name": "🖌️ 웹디자이너",
                "major": "디자인학과",
                "personality": "조용하지만 창의력이 뛰어남!",
                "salary": "평균 연봉 약 3,900만 원"
            }
        ]
    },

    "ESTP": {
        "jobs": [
            {
                "name": "💼 영업 전문가",
                "major": "경영학과",
                "personality": "사람 만나는 걸 좋아하고 활동적!",
                "salary": "평균 연봉 약 5,000만 원"
            },
            {
                "name": "🏀 스포츠 코치",
                "major": "체육학과",
                "personality": "에너지 넘치고 도전적인 성격!",
                "salary": "평균 연봉 약 4,200만 원"
            }
        ]
    },

    "ESFP": {
        "jobs": [
            {
                "name": "🎤 방송인",
                "major": "방송연예과",
                "personality": "사람들 앞에서 빛나는 스타일!",
                "salary": "평균 연봉 약 4,500만 원"
            },
            {
                "name": "🍰 파티 플래너",
                "major": "호텔관광학과",
                "personality": "분위기 메이커 역할을 잘함!",
                "salary": "평균 연봉 약 3,800만 원"
            }
        ]
    }
}

st.title("✨ MBTI 진로 추천 서비스 ✨")

st.write("안녕 😆")
st.write("너의 MBTI에 딱 맞는 진로를 추천해줄게!")
st.write("아래에서 MBTI를 선택해봐 👇")

mbti = st.selectbox(
    "🌈 MBTI 선택하기",
    list(mbti_data.keys())
)

if st.button("🔍 진로 추천 받기"):
    st.success(f"{mbti} 유형에게 어울리는 진로를 소개할게 😎")

    jobs = mbti_data[mbti]["jobs"]

    for job in jobs:
        st.markdown("---")
        st.subheader(job["name"])

        st.write(f"📚 추천 학과: {job['major']}")
        st.write(f"💖 잘 맞는 성격: {job['personality']}")
        st.write(f"💰 평균 연봉: {job['salary']}")

    st.balloons()

st.markdown("---")
st.caption("🌟 재미로 보는 추천이니까 너무 진지하게만 생각하지는 말기!")
