
import streamlit as st

st.title("OQYPH Prompt Generator")

object_desc = st.text_input("🎯 Object / Subject Description", 
                            "a black teddy bear with three eyes and green jelly cut surface")

combo = st.selectbox("🔑 Visual Combo", ["Freak + Cute", "Odd + Sacred", "Queer + Clinical", "Queer + Myth", "Freak + Soft", "Odd + Narcissism"])

ratio = st.selectbox("📐 Aspect Ratio", ["1:1", "2:3", "16:9"])

light_type = st.selectbox("💡 Light Type", ["soft flash", "harsh spotlight", "low key light"])

background_color = st.selectbox("🎨 Background Color", ["red background", "blue background", "black background", "white background"])

film_format = st.selectbox("🎞 Film Format", ["16mm", "35mm", "VHS"])

lens_type = st.selectbox("🔍 Lens Type", ["1970s 1980s vintage lens", "fish-eye lens", "macro lens"])

angle = st.selectbox("📷 Camera Angle", ["front view", "side view", "top view"])

# New pose inputs
overall_pose = st.selectbox("🕺 Overall Pose", ["", "standing", "sitting", "crouching", "jumping", "lying down"])
part_gesture = st.text_input("✋ Additional Part Gesture", "arm raised, head tilted")
direction = st.text_input("👁 Direction", "facing left")
energy = st.text_input("⚡ Energy / Mood", "dynamic pose")

# New frame size input
frame_size = st.selectbox("📏 Frame Size", [
    "", 
    "extreme close-up", 
    "close-up", 
    "bust shot", 
    "half-body shot", 
    "full-body shot", 
    "wide shot", 
    "extreme wide shot"
])

color_tone = "muted bruised pink and moldy mint"
extra_tone = "soft flash, stage-like composition"
grain = "high grain"

if st.button("✨ Generate Prompt"):
    pose_elements = [overall_pose, part_gesture.strip(), direction.strip(), energy.strip()]
    pose_filtered = [el for el in pose_elements if el]
    pose_description = ", ".join(pose_filtered)
    
    visual_tone = f"1970s 1980s film style, {film_format}, {lens_type}, handmade props, real texture, {grain}, {color_tone}, {extra_tone}, {light_type}, {background_color}, {angle}"
    
    if pose_description and frame_size:
        prompt = f"{object_desc}, {pose_description}, {frame_size}, {visual_tone} --ar {ratio}"
    elif pose_description:
        prompt = f"{object_desc}, {pose_description}, {visual_tone} --ar {ratio}"
    elif frame_size:
        prompt = f"{object_desc}, {frame_size}, {visual_tone} --ar {ratio}"
    else:
        prompt = f"{object_desc}, {visual_tone} --ar {ratio}"
    
    st.text_area("🎬 Generated Prompt", prompt, height=150)
