import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(
    page_title="서울 인구 분석",
    page_icon="📊",
    layout="wide"
)

st.title("📊 서울 연령별 인구 분석")

uploaded_file = st.file_uploader(
    "population.csv 파일 업로드",
    type=["csv"]
)

if uploaded_file is not None:

    # -------------------------
    # CSV 자동 인코딩/구분자 탐지
    # -------------------------
    encodings = [
        "utf-8",
        "utf-8-sig",
        "cp949",
        "euc-kr"
    ]

    separators = [
        ",",
        ";",
        "\t"
    ]

    df = None

    for enc in encodings:
        for sep in separators:
            try:
                uploaded_file.seek(0)

                temp_df = pd.read_csv(
                    uploaded_file,
                    encoding=enc,
                    sep=sep
                )

                # 컬럼이 최소 5개 이상이면 정상으로 판단
                if temp_df.shape[1] >= 5:
                    df = temp_df
                    detected_encoding = enc
                    detected_separator = sep
                    break

            except Exception:
                pass

        if df is not None:
            break

    if df is None:
        st.error("CSV 파일을 읽을 수 없습니다.")
        st.stop()

    st.success(
        f"인코딩: {detected_encoding} / 구분자: {repr(detected_separator)}"
    )

    # -------------------------
    # 컬럼명 정리
    # -------------------------
    df.columns = df.columns.str.strip()

    # 첫 번째 컬럼 = 행정구
    region_col = df.columns[0]

    # 총인구 컬럼 제거
    age_columns = []

    for col in df.columns:

        col_str = str(col)

        if (
            "~" in col_str
            or "이상" in col_str
        ):
            age_columns.append(col)

    if len(age_columns) == 0:
        st.error("연령대 컬럼을 찾을 수 없습니다.")
        st.write(df.columns.tolist())
        st.stop()

    # -------------------------
    # 행정구 선택
    # -------------------------
    regions = df[region_col].astype(str).tolist()

    selected_region = st.selectbox(
        "행정구 선택",
        regions
    )

    row = df[
        df[region_col].astype(str) == selected_region
    ].iloc[0]

    populations = []

    for col in age_columns:
        try:
            value = str(row[col]).replace(",", "")
            populations.append(float(value))
        except:
            populations.append(0)

    # -------------------------
    # 그래프
    # -------------------------
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=age_columns,
            y=populations,
            mode="lines+markers",
            line=dict(
                color="skyblue",
                width=4
            ),
            marker=dict(
                color="skyblue",
                size=8
            ),
            name="인구수"
        )
    )

    fig.update_layout(
        title=f"{selected_region} 연령별 인구",
        height=600,
        plot_bgcolor="#f2f2f2",
        paper_bgcolor="white",
        xaxis_title="나이",
        yaxis_title="인구수",
        hovermode="x unified",
        font=dict(size=14)
    )

    fig.update_xaxes(
        showgrid=True,
        gridcolor="white"
    )

    fig.update_yaxes(
        showgrid=True,
        gridcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # -------------------------
    # 데이터 테이블
    # -------------------------
    st.subheader("연령별 인구 데이터")

    result_df = pd.DataFrame({
        "연령대": age_columns,
        "인구수": populations
    })

    st.dataframe(
        result_df,
        use_container_width=True
    )

else:
    st.info("population.csv 파일을 업로드해주세요.")
