
import streamlit as st

st.title("OQYPH Prompt Generator")

# Inner elements (pose, scene, background)
st.markdown("## 🧍 Inner Elements (Pose / Scene / Background)")

overall_pose = st.selectbox("Overall Pose", ["", "standing", "sitting", "crouching", "jumping", "lying down"])
part_gesture = st.text_input("Part Gestures", "arm raised, head tilted")
direction = st.text_input("Direction", "facing left")
expression = st.text_input("Expression (e.g., neutral, smiling, screaming)", "neutral")
action = st.text_input("Action / Scene Interaction", "reaching toward light")
background_content = st.text_input("Background Content", "red background, church ruins")

object_desc = st.text_input("Object Description", 
                            "a black teddy bear with three eyes and green jelly cut surface")

st.markdown("---")

# Outer elements (camera, film, mood)
st.markdown("## 🎥 Outer Elements (Camera / Film / Mood)")

frame_size = st.selectbox("Frame Size", [
    "", 
    "extreme close-up", 
    "close-up", 
    "bust shot", 
    "half-body shot", 
    "full-body shot", 
    "wide shot", 
    "extreme wide shot"
])

angle = st.selectbox("Camera Angle", ["front view", "side view", "top view"])

film_format = st.selectbox("Film Format", ["16mm", "35mm", "VHS"])

lens_type = st.selectbox("Lens Type", ["1970s 1980s vintage lens", "fish-eye lens", "macro lens"])

light_type = st.selectbox("Lighting", ["soft flash", "harsh spotlight", "low key light"])

color_tone = st.text_input("Color Tone", "muted bruised pink and moldy mint")

grain = "high grain"
extra_tone = "soft flash, stage-like composition"

depth_effect = st.selectbox("Depth Effect", ["", "depth of field", "bokeh background"])
color_temperature = st.selectbox("Color Temperature / Filter", ["", "warm tone", "cold tone"])

if st.button("✨ Generate Prompt"):
    # Build inner description
    inner_elements = [overall_pose, part_gesture.strip(), direction.strip(), expression.strip(), action.strip(), background_content.strip()]
    inner_filtered = [el for el in inner_elements if el]
    inner_description = ", ".join(inner_filtered)
    
    # Build outer description
    outer_elements = [frame_size, angle, film_format, lens_type, depth_effect, color_temperature]
    outer_filtered = [el for el in outer_elements if el]
    outer_description = ", ".join(outer_filtered)
    
    visual_tone = f"1970s 1980s film style, handmade props, real texture, {grain}, {color_tone}, {extra_tone}, {light_type}"
    
    if inner_description and outer_description:
        prompt = f"{object_desc}, {inner_description}, {outer_description}, {visual_tone} --ar 2:3"
    elif inner_description:
        prompt = f"{object_desc}, {inner_description}, {visual_tone} --ar 2:3"
    elif outer_description:
        prompt = f"{object_desc}, {outer_description}, {visual_tone} --ar 2:3"
    else:
        prompt = f"{object_desc}, {visual_tone} --ar 2:3"
    
    st.text_area("🎬 Generated Prompt", prompt, height=150)
