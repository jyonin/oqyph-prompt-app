import streamlit as st
import random

st.title("OQYPH Prompt Generator")

# 풀 데이터
style_pool = ["eyeless", "deformed", "melted", "mirrored", "synthetic", "fragmented", "asymmetrical"]
target_pool = ["rabbit", "doll", "virgin mary", "statue", "angel", "cat", "unicorn", "mannequin"]
texture_pool = ["stone", "plastic doll", "fur toy", "vegetable", "flower", "liquid", "jelly"]

# 3컬럼 입력
col1, col2, col3 = st.columns(3)
adj = col1.selectbox("Visual Style (Adj.) / 형용사", [""] + style_pool)
target = col2.selectbox("Target / 대상", [""] + target_pool)
texture = col3.selectbox("Texture / 질감", [""] + texture_pool)

generated_scenario = ""

if st.button("🎲 Generate Random Scenario / 랜덤 시나리오 생성"):
    final_adj = adj if adj else random.choice(style_pool)
    final_target = target if target else random.choice(target_pool)
    final_texture = texture if texture else random.choice(texture_pool)
    generated_scenario = f"{final_adj} {final_target}, {final_texture} texture"
    st.text_area("Generated Scenario / 생성된 시나리오", generated_scenario, height=100)

# 추가: Object Description에 시나리오 자동 반영
st.markdown("---")
object_desc = st.text_input("Object Description / 대상 설명", generated_scenario if generated_scenario else "")
pose_desc = st.text_input("Pose Description / 포즈 및 액션", "standing, arm raised, facing left")
background = st.text_input("Background Content / 배경 내용", "red background, church ruins")
framing = st.text_input("Framing (size + aspect ratio) / 프레이밍", "close-up, 2:3")
angle = st.selectbox("Camera Angle / 카메라 앵글", ["front view", "side view", "top view", "back view"])
film = st.text_input("Film / lens / lighting / effects / 필름, 렌즈, 조명, 효과", 
                     "1970s 1980s film style, 16mm, vintage lens, soft flash")

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

    if removed:
        st.markdown("#### Removed duplicate elements / 제거된 중복 요소")
        st.write(", ".join(removed))
    else:
        st.markdown("✅ No duplicates found / 중복 요소 없음")
