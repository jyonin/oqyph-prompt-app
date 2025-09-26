{\rtf1\ansi\ansicpg949\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import streamlit as st\
import random\
from streamlit_drawable_canvas import st_canvas\
\
st.set_page_config(page_title="OQYPH Prompt Generator", layout="centered")\
st.title("OQYPH Prompt Generator")\
\
# \uc0\u45936 \u51060 \u53552  \u54400 \
odd_adjs = ["eyeless", "melted", "synthetic", "deformed", "fragmented", "asymmetrical", "distorted", "hollow", "cracked", "stretched", "burned", "fossilized", "corroded", "scorched", "grotesque"]\
odd_targets = ["doll", "rabbit", "mannequin", "virgin mary", "statue", "cat", "unicorn", "angel", "toy", "saint bust", "skull", "thorn crown", "broken mirror"]\
\
queer_adjs = ["ambiguous", "fluid", "androgynous", "twisted", "inverted", "mirrored", "hybrid", "reversed", "split", "reflected"]\
queer_targets = ["angel", "cherub", "idol", "mask", "mirror figure", "dual-faced statue", "serpent", "myth creature", "chimera"]\
\
freak_adjs = ["stitched", "mutated", "monstrous", "hybrid", "dismembered", "grotesque", "twisted", "scarred", "overgrown", "fused"]\
freak_targets = ["creature", "insect-human hybrid", "chimera", "stitched animal", "mutant doll", "beast", "limb pile", "eyeball cluster"]\
\
background_options = [\
    "red", "black", "green", "blue", "yellow", "orange", \
    "navy", "purple", "white", "gray", "rainbow gradient", \
    "background filled with jewels", \
    "velvet cloth in complementary color to object", \
    "white (isolated / no background)"\
]\
\
distance_options = [\
    "extreme close-up", "close-up", "bust shot", \
    "half-body shot", "full-body shot", "long shot", "extreme long shot"\
]\
\
lens_options_display = [\
    "\uc0\u55358 \u56809  16mm \u44305 \u44033  \u47116 \u51592  (\u50780 \u44257  \u44053 \u54632 , \u44277 \u44036 \u44048  \u44053 \u51312 )",\
    "\uc0\u55358 \u56708  35mm \u45796 \u53328  \u47116 \u51592  (\u51088 \u50672 \u49828 \u47084 \u50868  \u44305 \u44033 )",\
    "\uc0\u55357 \u56441  50mm \u54364 \u51456  \u47116 \u51592  (\u49324 \u46988  \u45576 \u44284  \u48708 \u49847 )",\
    "\uc0\u55358 \u56809  85mm \u51064 \u47932  \u47116 \u51592  (\u48176 \u44221  \u50517 \u52629 , \u48512 \u46300 \u47084 \u50880 )",\
    "\uc0\u55358 \u56708  200mm \u47581 \u50896  \u47116 \u51592  (\u50896 \u44540 \u44048  \u50557 \u54868 , \u50517 \u52629 )",\
    "\uc0\u55357 \u56441  fish-eye \u47116 \u51592  (\u44537 \u45800 \u51201  \u50780 \u44257 , \u52488 \u44305 \u44033 )",\
    "\uc0\u55358 \u56809  macro \u47116 \u51592  (\u52488 \u44540 \u51217  \u46356 \u53580 \u51068  \u44053 \u51312 )"\
]\
lens_options_clean = [\
    "16mm lens",\
    "35mm lens",\
    "50mm lens",\
    "85mm lens",\
    "200mm lens",\
    "fish-eye lens",\
    "macro lens"\
]\
\
# \uc0\u52852 \u53580 \u44256 \u47532 \u48324  \u50500 \u51060 \u53080 \
category_icons = \{"Odd": "\uc0\u55358 \u56809 ", "Queer": "\u55358 \u56708 ", "Freak": "\u55357 \u56441 "\}\
\
# \uc0\u52852 \u53580 \u44256 \u47532  \u49440 \u53469 \
adj_category = st.selectbox("Select adjective category / \uc0\u54805 \u50857 \u49324  \u52852 \u53580 \u44256 \u47532 ", ["Odd", "Queer", "Freak"], format_func=lambda x: f"\{category_icons[x]\} \{x\}")\
target_category = st.selectbox("Select target category / \uc0\u45824 \u49345  \u52852 \u53580 \u44256 \u47532 ", ["Odd", "Queer", "Freak"], format_func=lambda x: f"\{category_icons[x]\} \{x\}")\
\
# \uc0\u47004 \u45924  \u49373 \u49457  \u48260 \u53948 \u44284  \u44208 \u44284 \
if st.button("\uc0\u55356 \u57266  Generate Random Scenario"):\
    if adj_category == "Odd":\
        adj = random.choice(odd_adjs)\
    elif adj_category == "Queer":\
        adj = random.choice(queer_adjs)\
    else:\
        adj = random.choice(freak_adjs)\
\
    if target_category == "Odd":\
        target = random.choice(odd_targets)\
    elif target_category == "Queer":\
        target = random.choice(queer_targets)\
    else:\
        target = random.choice(freak_targets)\
\
    scenario = f"\{adj\} \{target\}"\
    st.session_state["scenario"] = scenario\
\
# \uc0\u49884 \u45208 \u47532 \u50724  \u52636 \u47141 \
scenario_display = st.session_state.get("scenario", "")\
st.text_area("Generated Scenario / \uc0\u49373 \u49457 \u46108  \u49884 \u45208 \u47532 \u50724 ", scenario_display, height=100)\
\
# \uc0\u52628 \u44032  \u51077 \u47141 \
background_color = st.selectbox("Select background / \uc0\u48176 \u44221  \u49440 \u53469 ", background_options)\
subject_distance = st.selectbox("Select subject distance / \uc0\u54588 \u49324 \u52404  \u44144 \u47532 ", distance_options)\
lens_idx = st.selectbox("Select lens type / \uc0\u47116 \u51592  \u51333 \u47448 ", lens_options_display, index=0)\
lens_clean = lens_options_clean[lens_options_display.index(lens_idx)]\
pose_desc = st.text_input("Pose Description / \uc0\u54252 \u51592  \u48143  \u50529 \u49496 ", "standing, arm raised, facing left")\
framing = st.selectbox("Framing / \uc0\u54868 \u47732  \u48708 \u50984 ", ["1:1", "2:3", "16:9"])\
angle = st.selectbox("Camera Angle / \uc0\u52852 \u47700 \u46972  \u50549 \u44544 ", ["front view", "side view", "top view", "back view"])\
\
# \uc0\u51060 \u48120 \u51648  \u50629 \u47196 \u46300  \u48143  \u51312 \u47749  \u50948 \u52824  \u51648 \u51221 \
st.subheader("\uc0\u51312 \u47749  \u50948 \u52824  \u51648 \u51221  (\u51060 \u48120 \u51648  \u50948  \u53364 \u47533 )")\
uploaded_img = st.file_uploader("\uc0\u51060 \u48120 \u51648  \u50629 \u47196 \u46300  (\u49440 \u53469 )", type=["png", "jpg", "jpeg"])\
canvas_result = None\
light_positions = []\
\
if uploaded_img:\
    st.image(uploaded_img, caption="\uc0\u50629 \u47196 \u46300 \u46108  \u51060 \u48120 \u51648 ", use_column_width=True)\
    canvas_result = st_canvas(\
        fill_color="rgba(255, 255, 0, 0.3)",  # \uc0\u51312 \u47749  \u47560 \u52964  \u49353 \u49345 \
        stroke_width=3,\
        background_image=uploaded_img,\
        update_streamlit=True,\
        height=400,\
        width=400,\
        drawing_mode="point",\
        point_display_radius=10,\
        key="canvas"\
    )\
    if canvas_result and canvas_result.json_data:\
        light_positions = [\
            (int(obj["left"]), int(obj["top"]))\
            for obj in canvas_result.json_data["objects"]\
            if obj["type"] == "circle"\
        ]\
        st.write(f"\uc0\u51648 \u51221 \u46108  \u51312 \u47749  \u50948 \u52824 : \{light_positions\}")\
\
# \uc0\u54532 \u47212 \u54532 \u53944  \u49373 \u49457 \
if st.button("\uc0\u10024  Generate Prompt"):\
    if scenario_display:\
        lens_film = f"\{lens_clean\}, 1970s 1980s vintage film style"\
        light_str = ""\
        if light_positions:\
            light_str = " | " + ", ".join([f"light source at (\{x\},\{y\})" for x, y in light_positions])\
        prompt = (\
            f"\{scenario_display\}, \{pose_desc\}, \{background_color\} background, "\
            f"\{subject_distance\}, \{angle\}, \{lens_film\} --ar \{framing\}\{light_str\}"\
        )\
        st.text_area("\uc0\u55356 \u57260  Generated Prompt / \u49373 \u49457 \u46108  \u54532 \u47212 \u54532 \u53944 ", prompt, height=150)\
    else:\
        st.warning("Please generate a scenario first!")}