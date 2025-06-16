import streamlit as st
import random

st.title("OQYPH Prompt Generator")

# 랜덤 시나리오 키워드 데이터
scenario_dict = {
    ("Odd", "Sacred"): [
        "eyeless virgin mary, black tears, plastic texture",
        "headless saint statue, melted surface, hollow eyes"
    ],
    ("Queer", "Myth"): [
        "synthetic unicorn, broken horn, metallic reflection",
        "androgynous angel, fragmented wings, neon halo"
    ],
    ("Freak", "Clinical"): [
        "stitched skin figure, anatomy tubes, translucent body",
        "asymmetrical face, medical mask, glass eyes"
    ],
    ("Odd", "Soft"): [
        "jelly-like cat, liquid eyes, rubbery texture",
        "plush rabbit, melted ear, soft glow"
    ],
    ("Narcissism", "Queer"): [
        "mirrored face mask, endless reflections, cracked surface",
        "fragmented body, chrome shine, double faces"
    ],
    # 추가 키워드 조합
    ("Freak", "Myth"): [
        "hybrid insect-human, ancient symbol tattoo, iridescent wings"
    ],
    ("Odd", "Clinical"): [
        "deformed doll, plastic tubes, hospital bed"
    ]
}

# 랜덤 시나리오 UI
st.markdown("## 🎲 OQYPH Random Scenario Generator / 랜덤 오키프 시나리오 생성기")
colA, colB = st.columns(2)
keyword1 = colA.selectbox("Visual Keyword 1 / 시각 키워드 1", ["", "Odd", "Freak", "Queer", "Sacred", "Clinical", "Myth", "Soft", "Narcissism"])
keyword2 = colB.selectbox("Visual Keyword 2 / 시각 키워드 2", ["", "Odd", "Freak", "Queer", "Sacred", "Clinical", "Myth", "Soft", "Narcissism"])

generated_scenario = ""
if st.button("🎲 Generate Random Scenario / 랜덤 시나리오 생성"):
    key_pair = (keyword1, keyword2)
    alt_pair = (keyword2, keyword1)
    candidates = scenario_dict.get(key_pair) or scenario_dict.get(alt_pair)
    if candidates:
        generated_scenario = random.choice(candidates)
        st.success("Scenario generated!")
    else:
        generated_scenario = "No scenario found for this combination."
    st.text_area("Generated OQYPH Scenario / 생성된 비주얼 시나리오", generated_scenario, height=100)

# 메인 컬럼
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧍 Inner Elements / 내부 요소")
    object_desc = st.text_input("Object Description / 대상 설명", generated_scenario if generated_scenario else "")
    pose_desc = st.text_input("Pose Description / 포즈 및 액션", "standing, arm raised, facing left")
    background = st.text_input("Background Content / 배경 내용", "red background, church ruins")

with col2:
    st.markdown("### 🎥 Outer Elements / 외부 요소")
    framing = st.text_input("Framing (size + aspect ratio) / 프레이밍", "close-up, 2:3")
    angle = st.selectbox("Camera Angle / 카메라 앵글", ["front view", "side view", "top view", "back view"])
    film = st.text_input("Film / lens / lighting / effects / 필름, 렌즈, 조명, 효과", 
                         "1970s 1980s film style, 16mm, vintage lens, soft flash")

# Generate button
if st.button("✨ Generate Prompt"):
    parts = f"{object_desc}, {pose_desc}, {background}, {framing}, {angle}, {film}"
    words = [w.strip() for w in parts.split(",")]

    seen = set()
    cleaned = []
    removed = []
    for w in words:
        if w not in seen:
            cleaned.append(w)
            seen.add(w)
        else:
            removed.append(w)

    final_prompt = ", ".join(cleaned)
    st.text_area("🎬 Generated Prompt / 생성된 프롬프트", final_prompt, height=150)

    # 복사 버튼 (Streamlit 환경에서는 JS나 클립보드 직접 접근 어려워 안내 제공)
    st.button("📋 Copy Prompt / 프롬프트 복사 (please copy manually)")

    # Removed duplicates
    if removed:
        st.markdown("#### Removed duplicate elements / 제거된 중복 요소")
        st.write(", ".join(removed))
    else:
        st.markdown("✅ No duplicates found / 중복 요소 없음")
