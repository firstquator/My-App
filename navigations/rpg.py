import random
import streamlit as st

# 환경 설정 관리
class Player:
    # 플레이어 데이터 관리
    PLAYER_IMG_SRC = "https://cdn.pixabay.com/photo/2021/10/19/13/12/squid-game-6723533_1280.png"

    def __init__(self, max_hp=100, max_mp=100):
        self.max_hp = max_hp
        self.max_mp = max_mp

        self.initialize_status()
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

    def down_mp(self, usage):
        st.session_state['mp'] -= usage
        if st.session_state['mp'] < 0:
            st.session_state['mp'] = 0
            
        self.update_html()

    def initialize_status(self):
        if 'hp' not in st.session_state:
            st.session_state['hp'] = self.max_hp

        if 'mp' not in st.session_state:
            st.session_state['mp'] = self.max_mp

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
                    width: {st.session_state['mp']}%;
                    height: 100%;
                    background-color: #2980b9;            
                '></div>
            </div>
        </div>
        """

class Enemy:
    def __init__(self, name, max_hp=100):
        if name == '고블린':
            self.enemy_src = 'https://cdn.pixabay.com/photo/2021/10/22/03/53/creature-6731005_1280.png'
        elif name == '골렘':
            self.enemy_src = 'https://static.wikia.nocookie.net/maplestorym/images/5/53/%EB%AA%AC%EC%8A%A4%ED%84%B0_%EC%95%84%EC%9D%B4%EC%8A%A4_%EB%AF%B9%EC%8A%A4%EA%B3%A8%EB%A0%98.png/revision/latest/thumbnail/width/360/height/450?cb=20180201160002&path-prefix=ko'
        
        self.max_hp = max_hp
        self.initialize_status()
        self.ENEMY_HTML = f"""
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
            src='{self.enemy_src}' 
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
        </div>
        """

    def draw(self, container=None):
        if container:
            container.markdown(self.ENEMY_HTML, unsafe_allow_html=True)
        else:
            st.markdown(self.ENEMY_HTML, unsafe_allow_html=True)

    def down_hp(self, damage):
        st.session_state['enemy_hp'] -= damage
        if st.session_state['enemy_hp'] < 0:
            st.session_state['enemy_hp'] = 0
            
        self.update_html()

    def initialize_status(self):
        if 'enemy_hp' not in st.session_state:
            st.session_state['enemy_hp'] = self.max_hp

    def update_html(self):
        self.ENEMY_HTML = f"""
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
            src='{self.enemy_src}' 
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
                    width: {st.session_state['enemy_hp']}%;
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
                    width: {st.session_state['mp']}%;
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

# 플레이어, 몬스터 객체 생성하기
player = Player()
enemy = Enemy(name='고블린')

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
    enemy.draw()

# 가챠!
col3, col4 = st.columns(2)

with col3:
    item_path = 'https://cdn2.iconfinder.com/data/icons/retro-game-items-revamp-border/100/sword_hero_weapon_attack_blade-512.png'
    gacha_html = f"""
        <div style="
            height: 500px;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            border: 3px solid yellow;
        ">
            <img src="{item_path}"
            style="
               width: 100px;
               height: 100px; 
            ">
            <p>공격 : 20</p>
        </div>
    """

    st.markdown(gacha_html, unsafe_allow_html=True)