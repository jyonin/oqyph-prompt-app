import streamlit as st
import random

st.title("OQYPH Prompt Generator")

# 키워드 풀
odd_adjs = ["eyeless", "melted", "synthetic", "deformed", "fragmented", "asymmetrical", "distorted", "hollow", "cracked", "stretched", "burned", "fossilized", "corroded", "scorched", "grotesque"]
odd_targets = ["doll", "rabbit", "mannequin", "virgin mary", "statue", "cat", "unicorn", "angel", "toy", "saint bust", "skull", "thorn crown", "broken mirror"]

queer_adjs = ["ambiguous", "fluid", "androgynous", "twisted", "inverted", "mirrored", "hybrid", "reversed", "split", "reflected"]
queer_targets = ["angel", "cherub", "idol", "mask", "mirror figure", "dual-faced statue", "serpent", "myth creature", "chimera"]

freak_adjs = ["stitched", "mutated", "monstrous", "hybrid", "dismembered", "grotesque", "twisted", "scarred", "overgrown", "fused"]
freak_targets = ["creature", "insect-human hybrid", "chimera", "stitched animal", "mutant doll", "beast", "limb pile", "eyeball cluster"]

textures = ["jelly", "plastic doll", "stone", "fur toy", "liquid", "vegetable", "flower", "bone", "rusted metal", "wax"]

# 랜덤 생성
if st.button("🎲 Generate Random OQYPH Scenario"):
    adjs = random.sample(odd_adjs, 1) + random.sample(queer_adjs, 1) + random.sample(freak_adjs, 1)
    targets = random.sample(odd_targets, 1) + random.sample(queer_targets, 1) + random.sample(freak_targets, 1)
    texture = random.choice(textures)

    scenario = f"{', '.join(adjs)} {', '.join(targets)}, {texture} texture"
    st.text_area("Generated Scenario / 생성된 시나리오", scenario, height=100)

    # 추가 정보
    pose_desc = st.text_input("Pose Description / 포즈 및 액션", "standing, arm raised, facing left")
    background = st.text_input("Background Content / 배경 내용", "red background, church ruins")
    framing = st.selectbox("Framing / 화면 비율", ["1:1", "2:3", "16:9"])
    angle = st.selectbox("Camera Angle / 카메라 앵글", ["front view", "side view", "top view", "back view"])
    film = st.text_input("Film / lens / lighting / effects", "1970s 1980s film style, 16mm, vintage lens, soft flash")

    if st.button("✨ Generate Prompt"):
        prompt = f"{scenario}, {pose_desc}, {background}, {angle}, {film} --ar {framing}"
        st.text_area("🎬 Generated Prompt / 생성된 프롬프트", prompt, height=150)
