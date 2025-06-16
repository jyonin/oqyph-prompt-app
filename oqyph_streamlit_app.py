import streamlit as st
import random

st.title("OQYPH Prompt Generator")

odd_adjs = ["eyeless", "melted", "synthetic", "deformed", "mirrored", "fragmented"]
freak_targets = ["rabbit", "doll", "mannequin", "virgin mary", "statue", "angel"]
textures = ["jelly", "plastic doll", "stone", "fur toy", "liquid", "vegetable", "flower"]

generated_scenario = ""

if st.button("🎲 Generate Random OQYPH Scenario / 랜덤 오키프 시나리오 생성"):
    adj_sample = random.sample(odd_adjs, 3)
    target_sample = random.sample(freak_targets, 3)
    texture_sample = random.choice(textures)
    
    generated_scenario = f"{', '.join(adj_sample)} {', '.join(target_sample)}, {texture_sample} texture"
    st.text_area("Generated Scenario / 생성된 시나리오", generated_scenario, height=100)

# Main inputs
st.markdown("---")
object_desc = st.text_input("Object Description / 대상 설명", generated_scenario if generated_scenario else "")
pose_desc = st.text_input("Pose Description / 포즈 및 액션", "standing, arm raised, facing left")
background = st.text_input("Background Content / 배경 내용", "red background, church ruins")

framing = st.selectbox("Framing / 화면 비율", ["1:1", "2:3", "16:9"])
angle = st.selectbox("Camera Angle / 카메라 앵글", ["front view", "side view", "top view", "back view"])
film = st.text_input("Film / lens / lighting / effects", "1970s 1980s film style, 16mm, vintage lens, soft flash")

if st.button("✨ Generate Prompt"):
    parts = f"{object_desc}, {pose_desc}, {background}, {angle}, {film}"
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

    ar_code = f"--ar {framing}" if framing else ""
    final_prompt = ", ".join(cleaned) + f" {ar_code}"
    st.text_area("🎬 Generated Prompt / 생성된 프롬프트", final_prompt, height=150)

    if removed:
        st.markdown("#### Removed duplicate elements / 제거된 중복 요소")
        st.write(", ".join(removed))
    else:
        st.markdown("✅ No duplicates found / 중복 요소 없음")
