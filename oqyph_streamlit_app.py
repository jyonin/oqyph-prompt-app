# 버튼 클릭 시 session_state에 저장
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

# 시나리오 출력
scenario_display = st.session_state.get("scenario", "")
st.text_area("Generated Scenario / 생성된 시나리오", scenario_display, height=100)

# 최종 프롬프트 생성
if st.button("✨ Generate Prompt"):
    pose_desc = st.text_input("Pose Description / 포즈 및 액션", "standing, arm raised, facing left", key="pose_input")
    background = st.text_input("Background Content / 배경 내용", "red background, church ruins", key="bg_input")
    framing = st.selectbox("Framing / 화면 비율", ["1:1", "2:3", "16:9"], key="frame_input")
    angle = st.selectbox("Camera Angle / 카메라 앵글", ["front view", "side view", "top view", "back view"], key="angle_input")
    film = st.text_input("Film / lens / lighting / effects", "1970s 1980s film style, 16mm, vintage lens, soft flash", key="film_input")

    prompt = f"{scenario_display}, {pose_desc}, {background}, {angle}, {film} --ar {framing}"
    st.text_area("🎬 Generated Prompt / 생성된 프롬프트", prompt, height=150)
