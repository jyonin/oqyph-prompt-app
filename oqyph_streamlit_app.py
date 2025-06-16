import streamlit as st

st.title("OQYPH Prompt Generator")

# Inner elements
st.markdown("## 🧍 Inner Elements (Pose / Scene / Background)")

# Overall pose: 선택 + 자유 입력
overall_pose_select = st.selectbox("Overall Pose (Select)", ["", "standing", "sitting", "crouching", "jumping", "lying down"])
overall_pose_custom = st.text_input("Overall Pose (Custom, optional)", "")

part_gesture = st.text_input("Part Gestures", "arm raised, head tilted")
direction = st.text_input("Direction", "facing left")
expression = st.text_input("Expression", "neutral")
action = st.text_input("Action / Scene Interaction", "reaching toward light")
background_content = st.text_input("Background Content", "red background, church ruins")

object_desc = st.text_input("Object Description", 
                            "a black teddy bear with three eyes and green jelly cut surface")

st.markdown("---")

# Outer elements
st.markdown("## 🎥 Outer Elements (Camera / Film / Mood)")

# Frame size = 화면 비율
frame_ratio = st.selectbox("Frame Aspect Ratio", ["", "1:1", "2:3", "16:9"])

# Subject size
subject_size = st.selectbox("Subject Size", [
    "", 
    "extreme close-up", 
    "close-up", 
    "bust shot", 
    "half-body shot", 
    "full-body shot", 
    "wide shot", 
    "extreme wide shot"
])

angle = st.selectbox("Camera Angle", ["front view", "side view", "top view", "back view"])
film_format = st.selectbox("Film Format", ["16mm", "35mm", "VHS"])
lens_type = st.selectbox("Lens Type", ["1970s 1980s vintage lens", "fish-eye lens", "macro lens"])
light_type = st.selectbox("Lighting", ["soft flash", "harsh spotlight", "low key light"])
color_tone = st.text_input("Color Tone", "muted bruised pink and moldy mint")

grain = "high grain"
extra_tone = "soft flash, stage-like composition"

depth_effect = st.selectbox("Depth Effect", ["", "depth of field", "bokeh background"])
color_temperature = st.selectbox("Color Temperature / Filter", ["", "warm tone", "cold tone"])

if st.button("✨ Generate Prompt"):
    # Build inner
    poses = [overall_pose_select, overall_pose_custom.strip()]
    pose_combined = ", ".join([p for p in poses if p])
    
    inner_elements = [pose_combined, part_gesture.strip(), direction.strip(), expression.strip(), action.strip(), background_content.strip()]
    inner_filtered = [el for el in inner_elements if el]
    inner_description = ", ".join(inner_filtered)
    
    # Build outer
    outer_elements = [frame_ratio, subject_size, angle, film_format, lens_type, depth_effect, color_temperature]
    outer_filtered = [el for el in outer_elements if el]
    outer_description = ", ".join(outer_filtered)
    
    visual_tone = f"1970s 1980s film style, handmade props, real texture, {grain}, {color_tone}, {extra_tone}, {light_type}"
    
    prompt_parts = [object_desc]
    if inner_description:
        prompt_parts.append(inner_description)
    if outer_description:
        prompt_parts.append(outer_description)
    prompt_parts.append(visual_tone + f" --ar {frame_ratio if frame_ratio else '2:3'}")
    
    prompt = ", ".join(prompt_parts)
    
    st.text_area("🎬 Generated Prompt", prompt, height=150)
