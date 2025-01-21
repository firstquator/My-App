# https://docs.streamlit.io/develop/api-reference
import streamlit as st
import random

def display_chat(user_mes, friend_mes):
    user = st.chat_message('user')
    friend = st.chat_message('ai')

    user.write(user_mes)
    friend.write(friend_mes)

def save_chat(user_mes, friend_mes):
    st.session_state['message_box'].append(
        {
            "user": user_mes,
            "friend": friend_mes
        }
    )

st.set_page_config(
    page_title="HOME",
    page_icon="🏠",
    layout='wide'
)

message_examples = [
    "안녕하세요!",
    "저는 바보에요!",
    "나가주실래요 ?",
    "죽어주세요!!",
    "돈 내놔."
]

# 채팅 기능
# - 입력할 수 있는 칸
# - 상대방 ( 누가 들어와 있는지 확인 )
if 'message_box' not in st.session_state:
    st.session_state['message_box'] = []

message = st.chat_input()
if message:
    friend_message = random.choice(message_examples)

    for mes in st.session_state['message_box']:
        display_chat(mes['user'], mes['friend'])
        st.markdown('---')


    display_chat(message, friend_message)
    save_chat(message, friend_message)