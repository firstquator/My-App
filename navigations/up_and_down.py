import random
import streamlit as st

start_btn = 0
init_btn = 0
correct = 0

if 'is_start' not in st.session_state:
    st.session_state['is_start'] = False

if 'try' not in st.session_state:
    st.session_state['try'] = 0

# 게임시작 버튼
if not st.session_state['is_start']:
    start_btn = st.button("🎃 게임 시작!")
else:
    init_btn = st.button("🔍 초기화")

if start_btn:
    st.session_state['is_start'] = True
if init_btn:
    st.session_state['is_start'] = False
    st.session_state['try'] = 0
    
if st.session_state['is_start']:
    # 정답 숫자를 정해줘야 함. (랜덤으로)
    if 'correct' not in st.session_state:
        correct = random.randint(1, 50)
        st.session_state['correct'] = correct
    else:
        correct = st.session_state['correct']

    # 입력 공간이 필요.
    answer = st.text_input("🏓 정답 입력", placeholder="1 ~ 50 까지의 숫자만 입력")

    # UP & DOWN 알고리즘
    if answer:
        answer = int(answer)

        if answer > correct:
            st.markdown("# DOWN")
            st.session_state['try'] += 1
        elif answer < correct:
            st.markdown("# UP")
            st.session_state['try'] += 1
        else:
            st.markdown(f"# 정답!! {st.session_state['try']}번 시도하셨습니다.")