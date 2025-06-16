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

background_options = [
    "red", "black", "green", "blue", "yellow", "orange", 
    "navy", "purple", "white", "gray", "rainbow gradient", 
    "background filled with jewels", 
    "velvet cloth in complementary color to object", 
    "white (isolated / no background)"
]

distance_options = [
    "extreme close-up", "close-up", "bust shot", 
    "half-body shot", "full-body shot", "long shot", "extreme long shot"
]

lens_options = [
    "16mm 광각 렌즈 (왜곡 강함, 공간감 강조)",
    "35mm 다큐 렌즈 (자연스러운 광각)",
    "50mm 표준 렌즈 (사람 눈과 비슷)",
    "85mm 인물 렌즈 (배경 압축, 부드러움)",
    "200mm 망원 렌즈 (원근감 약화, 압축)",
    "fish-eye 렌즈 (극단적 왜곡, 초광각)",
    "macro 렌즈 (초근접 디테일 강조)"
]

# 카테고리 선택
adj_category = st.selectbox("Select adjective category / 형용사 카테고리", ["Odd", "Queer", "Freak"])
target_category = st.selectbox("Select target category / 대상 카테고리", ["Odd", "Queer", "Freak"])

# 랜덤 생성 버튼과 결과
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

    scenario = f"{adj} {target}"
    st.session_state["scenario"] = scenario

# 시나리오 출력
scenario_display = st.session_state.get("scenario", "")
st.text_area("Generated Scenario / 생성된 시나리오", scenario_display, height=100)

# 추가 입력
background_color = st.selectbox("Select background / 배경 선택", background_options)
subject_distance = st.selectbox("Select subject distance / 피사체 거리", distance_options)
lens_choice = st.selectbox("Select lens type / 렌즈 종류", lens_options)
pose_desc = st.text_input("Pose Description / 포즈 및 액션", "standing, arm raised, facing left")
framing = st.selectbox("Framing / 화면 비율", ["1:1", "2:3", "16:9"])
angle = st.selectbox("Camera Angle / 카메라 앵글", ["front view", "side view", "top view", "back view"])

# 프롬프트 생성
if st.button("✨ Generate Prompt"):
    if scenario_display:
        lens_film = f"{lens_choice}, 1970s 1980s vintage film style"
        prompt = (
            f"{scenario_display}, {pose_desc}, {background_color} background, "
            f"{subject_distance}, {angle}, {lens_film} --ar {framing}"
        )
        st.text_area("🎬 Generated Prompt / 생성된 프롬프트", prompt, height=150)
    else:
        st.warning("Please generate a scenario first!")
