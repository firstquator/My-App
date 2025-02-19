import random, time
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

def get_gacha_html(info):
    return f"""
            <div style="
                height: 500px;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                border: 3px solid yellow;
            ">
                <img src="{info['img_path']}"
                style="
                width: 100px;
                height: 100px; 
                ">
                <p>{info['effect'][0]}</p>
            </div>
        """

def item_draw_action(item_list, times=3, sec=0.1):
    screen = st.empty()
    for item in item_list*times:
        screen.markdown(get_gacha_html(item), unsafe_allow_html=True)
        time.sleep(sec)
        screen.empty()
    
    return screen

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
if "num_draw" not in st.session_state:
    st.session_state['num_draw'] = 10
item_list = [
    {
        "effect": ["공격", 20],
        "img_path": 'https://cdn2.iconfinder.com/data/icons/retro-game-items-revamp-border/100/sword_hero_weapon_attack_blade-512.png',
        "prob": 1
    },
    {
        "effect": ["꽝", 0],
        "img_path": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDp3BDp-i-Pyull-FDYT5PkZdOEXEDzywyag&s",
        "prob": 10
    }
]

item_box = []
for item in item_list:
    copy = [item] * item['prob']
    item_box += copy

result = random.choice(item_box)

col3, col4 = st.columns(2)

with col3:
    draw_btn = st.button('뽑기!')
    st.markdown(f"남은 뽑기 : {st.session_state['num_draw']}")

with col4:
    if draw_btn and st.session_state['num_draw'] > 0:
        st.session_state['num_draw'] -= 1
        
        screen = item_draw_action(item_list, 10, 0.05)

        gacha_html = get_gacha_html(result)
        screen.markdown(gacha_html, unsafe_allow_html=True)

    elif st.session_state['num_draw'] <= 0:
        reset_btn = st.button("뽑기권 충전!")

        if reset_btn:
            st.session_state['num_draw'] = 10

st.write(result)