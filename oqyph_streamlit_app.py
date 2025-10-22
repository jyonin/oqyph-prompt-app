
import streamlit as st
import random
from streamlit_drawable_canvas import st_canvas

st.set_page_config(page_title="OQYPH Prompt Generator", layout="centered")
st.title("OQYPH Prompt Generator")

# 형용사 및 대상 리스트
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

lens_options_display = [
    "📷 16mm 렌즈 (광각, 과장된 원근감)",
    "📸 35mm 렌즈 (자연스러운 시야각)",
    "📷 50mm 렌즈 (눈에 가까운 화각)",
    "📸 85mm 렌즈 (인물용, 배경 흐림)",
    "📷 200mm 렌즈 (먼거리 촬영, 인물특화)",
    "📸 fish-eye 렌즈 (광각 왜곡)",
    "📷 macro 렌즈 (초근접 촬영)"
]
lens_options_clean = [
    "16mm lens",
    "35mm lens",
    "50mm lens",
    "85mm lens",
    "200mm lens",
    "fish-eye lens",
    "macro lens"
]

category_icons = {"Odd": "📷", "Queer": "📸", "Freak": "📷"}

adj_category = st.selectbox("Select adjective category / 형용사 카테고리", ["Odd", "Queer", "Freak"], format_func=lambda x: f"{category_icons[x]} {x}")
target_category = st.selectbox("Select target category / 대상 카테고리", ["Odd", "Queer", "Freak"], format_func=lambda x: f"{category_icons[x]} {x}")

if st.button("✨ Generate Random Scenario"):
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

scenario_display = st.session_state.get("scenario", "")
st.text_area("Generated Scenario / 생성된 시나리오", scenario_display, height=100)

background_color = st.selectbox("Select background / 배경 선택", background_options)
subject_distance = st.selectbox("Select subject distance / 피사체 거리", distance_options)
lens_idx = st.selectbox("Select lens type / 렌즈 종류", lens_options_display, index=0)
lens_clean = lens_options_clean[lens_options_display.index(lens_idx)]
pose_desc = st.text_input("Pose Description / 자세 묘사", "standing, arm raised, facing left")
framing = st.selectbox("Framing / 화면비율", ["1:1", "2:3", "16:9"])
angle = st.selectbox("Camera Angle / 카메라 앵글", ["front view", "side view", "top view", "back view"])

st.subheader("📷 조명 위치 지정 (선택 사항)")
uploaded_img = st.file_uploader("이미지 업로드 (선택)", type=["png", "jpg", "jpeg"])
canvas_result = None
light_positions = []

if uploaded_img:
    st.image(uploaded_img, caption="업로드한 이미지", use_column_width=True)
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 0, 0.3)",
        stroke_width=3,
        background_image=uploaded_img,
        update_streamlit=True,
        height=400,
        width=400,
        drawing_mode="point",
        point_display_radius=10,
        key="canvas"
    )
    if canvas_result and canvas_result.json_data:
        light_positions = [
            (int(obj["left"]), int(obj["top"]))
            for obj in canvas_result.json_data["objects"]
            if obj["type"] == "circle"
        ]
        st.write(f"지정된 조명 위치: {light_positions}")

if st.button("✨ Generate Prompt"):
    if scenario_display:
        lens_film = f"{lens_clean}, 1970s 1980s vintage film style"
        light_str = ""
        if light_positions:
            light_str = " | " + ", ".join([f"light source at ({x},{y})" for x, y in light_positions])
        prompt = (
            f"{scenario_display}, {pose_desc}, {background_color} background, "
            f"{subject_distance}, {angle}, {lens_film} --ar {framing}{light_str}"
        )
        st.text_area("✨ Generated Prompt / 생성된 프롬프트", prompt, height=150)
    else:
        st.warning("Please generate a scenario first!")
