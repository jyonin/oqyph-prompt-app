
import streamlit as st

st.title("OQYPH Prompt Generator")

object_desc = st.text_input("🎯 Object / Subject Description", 
                            "a black teddy bear with three eyes and green jelly cut surface")

combo = st.selectbox("🔑 Visual Combo", ["Freak + Cute", "Odd + Sacred", "Queer + Clinical", "Queer + Myth", "Freak + Soft", "Odd + Narcissism"])

ratio = st.selectbox("📐 Aspect Ratio", ["2:3", "16:9"])

light_type = st.selectbox("💡 Light Type", ["soft flash", "harsh spotlight", "low key light"])

background_color = st.selectbox("🎨 Background Color", ["red background", "blue background", "black background", "white background"])

film_format = st.selectbox("🎞 Film Format", ["16mm", "35mm", "VHS"])

lens_type = st.selectbox("🔍 Lens Type", ["1970s 1980s vintage lens", "fish-eye lens", "macro lens"])

angle = st.selectbox("📷 Camera Angle", ["front view", "side view", "top view"])

color_tone = "muted bruised pink and moldy mint"
extra_tone = "soft flash, stage-like composition"
grain = "high grain"

if st.button("✨ Generate Prompt"):
    visual_tone = f"1970s 1980s film style, {film_format}, {lens_type}, handmade props, real texture, {grain}, {color_tone}, {extra_tone}, {light_type}, {background_color}, {angle}"
    prompt = f"{object_desc}, {visual_tone} --ar {ratio}"
    st.text_area("🎬 Generated Prompt", prompt, height=150)
