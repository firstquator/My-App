import random
import streamlit as st

st.set_page_config(
    page_title='up and down game',
    page_icon='👍👎',
)

# 게임 목숨
max_life=6
if 'life' not in st.session_state:
    st.session_state['life'] = max_life

# 정답 숫자 (랜덤으로.)
if 'correct' not in st.session_state:
    st.session_state['correct'] = random.randint(1, 50)

# 숫자 입력
answer = st.chat_input("1 ~ 50까지 숫자 중 하나를 입력하세요.")

# UP & DOWN & 정답
if answer:
    if int(answer) < st.session_state['correct']:
        result = "UP"
        st.session_state['life'] -= 1
        if st.session_state['life'] < 0:
            st.session_state['life'] = 0
    elif int(answer) > st.session_state['correct']:
        result = "DOWN"
        st.session_state['life'] -= 1
        if st.session_state['life'] < 0:
            st.session_state['life'] = 0
    else:
        result = "정답"
        st.balloons()

    if st.session_state['life']:
        have_life = "🟢" * st.session_state['life']
        lost_life = "🔴" * (max_life - st.session_state['life'])
        st.markdown(f"### {have_life + lost_life}")

    player = st.chat_message('human')
    player.markdown(f"**{answer}**")

    ai = st.chat_message('ai')
    ai.markdown(f"**{result}**")

    if st.session_state['life'] <= 0:
        st.image("https://blog.kakaocdn.net/dn/miKTq/btq0pxYHXre/OLKofF0Qc9wUj8M74mulh1/img.jpg")