import random
import streamlit as st

# 환경 설정 관리
class Player:
    # 플레이어 데이터 관리
    PLAYER_IMG_SRC = "https://cdn.pixabay.com/photo/2021/10/19/13/12/squid-game-6723533_1280.png"

    def __init__(self, max_hp=100):
        if 'hp' not in st.session_state:
            st.session_state['hp'] = max_hp

        self.max_hp = max_hp
        self.PLAYER_HTML = f"""
        <div 
        style='
            display:flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            width: 300px;
            height: 600px;
        '
        >
            <!-- 캐릭터 -->
            <img 
            src='{self.PLAYER_IMG_SRC}' 
            style='
                width: 80%;
                margin-bottom: 20px;
            '>
            <!-- HP BAR -->
            <div
            style='
                width: 80%;
                height: 30px;
                border: 3px solid #ecf0f1;
                border-radius: 15px;
                overflow: hidden;
                margin-bottom: 15px;
            '>
                <div
                style='
                    width: 100%;
                    height: 100%;
                    background-color: #2ecc71;            
                '></div>
            </div>
            <!-- MP BAR -->
            <div
            style='
                width: 80%;
                height: 30px;
                border: 3px solid #ecf0f1;
                border-radius: 15px;
                overflow: hidden;
            '>
                <div
                style='
                    width: 100%;
                    height: 100%;
                    background-color: #2980b9;            
                '></div>
            </div>
        </div>
        """

    def draw(self, container=None):
        if container:
            container.markdown(self.PLAYER_HTML, unsafe_allow_html=True)
        else:
            st.markdown(self.PLAYER_HTML, unsafe_allow_html=True)

    def down_hp(self, damage):
        st.session_state['hp'] -= damage
        if st.session_state['hp'] < 0:
            st.session_state['hp'] = 0
            
        self.update_html()

    def update_html(self):
        self.PLAYER_HTML = f"""
        <div 
        style='
            display:flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            width: 300px;
            height: 600px;
        '
        >
            <!-- 캐릭터 -->
            <img 
            src='{self.PLAYER_IMG_SRC}' 
            style='
                width: 80%;
                margin-bottom: 20px;
            '>
            <!-- HP BAR -->
            <div
            style='
                width: 80%;
                height: 30px;
                border: 3px solid #ecf0f1;
                border-radius: 15px;
                overflow: hidden;
                margin-bottom: 15px;
            '>
                <div
                style='
                    width: {st.session_state['hp']}%;
                    height: 100%;
                    background-color: #2ecc71;            
                '></div>
            </div>
            <!-- MP BAR -->
            <div
            style='
                width: 80%;
                height: 30px;
                border: 3px solid #ecf0f1;
                border-radius: 15px;
                overflow: hidden;
            '>
                <div
                style='
                    width: 100%;
                    height: 100%;
                    background-color: #2980b9;            
                '></div>
            </div>
        </div>
        """


# 웹페이지 세팅
st.set_page_config(
    page_title="RPG",
    page_icon="🏹",
    layout='wide'
)

player = Player()

# RPG / 포켓몬 게임 전투 스타일
# UI
col1, col2 = st.columns(2)

# MY 캐릭터
with col1:
    container = st.container(border=True)
    test_btn = st.button("HP 감소")
    if test_btn:
        player.down_hp(random.randint(5, 30))  

    player.draw()
    

with col2:
    pass