import random
import streamlit as st

st.set_page_config(
    page_title='Lotto 생성기',
    page_icon='💵',
    layout='wide'
)

def display_lottory(background="#16C47F", border="#FFD65A"):
    lottery = []
    # 6개의 랜덤한 숫자를 뽑는 것.
    while len(lottery) < 6:
        num = random.randint(1, 45)

        if num not in lottery:
            lottery.append(num)

    # 뽑은 숫자들을 나열
    container = st.container(border=True)
    cols = container.columns(6)
    for col, lotto in zip(cols, lottery):
        col.markdown(f"""
            <div style='
                display: flex;
                justify-content: center;
                margin-bottom: 10px;
            '>
                <div style='
                    width: 50px;
                    height: 50px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    background-color: {background};
                    border-radius: 50%;
                    border: 2px solid {border};
                    font-weight: 800;
                '>
                    {lotto}
                </div>        
            </div>
        """, unsafe_allow_html=True)

# 로또 생성
lotto_btn = st.button("🟢 로또 생성기")

if lotto_btn:
    for i in range(2):
        display_lottory(background="#85A947", border="#A9BFA8")

        
