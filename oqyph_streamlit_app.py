import streamlit as st
import random

st.title("OQYPH Prompt Generator")

# 데이터 풀
odd_adjs = ["eyeless", "melted", "synthetic", "deformed", "fragmented", "asymmetrical", "distorted", "hollow", "cracked", "stretched", "burned", "fossilized", "corroded", "scorched", "grotesque"]
odd_targets = ["doll", "rabbit", "mannequin", "virgin mary", "statue", "cat", "unicorn", "angel", "toy", "saint bust", "skull", "thorn crown", "broken mirror"]

queer_adjs = ["ambiguous", "fluid", "androgynous", "twisted", "inverted", "mirrored", "hybrid", "reversed", "split", "reflected"]
queer_targets = ["angel", "cherub", "idol", "mask", "mirror figure", "dual-faced statue", "serpent", "myth creature", "chimera"]

freak_adjs = ["stitched", "mutated", "monstrous", "hybrid", "dismembered", "grotesque", "twisted", "scarred", "overgrown", "fused"]
freak_targets = ["creature", "insect-human hybrid", "chimera", "stitched animal", "mutant doll", "beast", "limb pile", "eyeball cluster"]

textures = ["jelly", "plastic doll", "stone", "fur toy", "liquid", "vegetable", "flower", "bone", "rusted metal", "wax"]

# 카테고리 선택
adj_category = st.selectbox("Select adjective category / 형용사 카테고리", ["Odd", "Queer", "Freak"])
target_category = st.selectbox("Select target category / 대상 카테고리", ["Odd", "Queer", "Freak"])
texture_choice = st.selectbox("Select texture / 텍스처 선택", textures)

# 랜덤 요소 생성
if st.button("🎲 Generate Random Scenario"):
    if adj_category == "Odd":
        adj = random.choice(odd_adjs)
    elif adj_category == "Queer":
        adj = random.choice(queer_adjs)
    else:
        adj = random.choice(freak_adjs)

    if target_category == "Odd":
        target = random.choice(odd_targets)
    elif target_category == "Queer":
        target = random.choice(queer_targets)
    else:
        target = random.choice(freak_targets)

    scenario = f"{adj} {target}, {texture_choice} texture"
    st.session_state["scenario"] = scenario

# 시나리오 출력 유지
scenario_display = st.session_state.get("scenario", "")
st.text_area("Generated Scenario / 생성된 시나리오", scenario_display, height=100)

# 추가 요소
pose_desc = st.text_input("Pose Description / 포즈 및 액션", "standing, arm raised, facing left")
background = st.text_input("Background Content / 배경 내용", "red background, church ruins")
framing = st.selectbox("Framing / 화면 비율", ["1:1", "2:3", "16:9"])
angle = st.selectbox("Camera Angle / 카메라 앵글", ["front view", "side view", "top view", "back view"])
film = st.text_input("Film / lens / lighting / effects", "1970s 1980s film style, 16mm, vintage lens, soft flash")

# 프롬프트 생성
if st.button("✨ Generate Prompt"):
    if scenario_display:
        prompt = f"{scenario_display}, {pose_desc}, {background}, {angle}, {film} --ar {framing}"
        st.text_area("🎬 Generated Prompt / 생성된 프롬프트", prompt, height=150)
    else:
        st.warning("Please generate a scenario first!")
