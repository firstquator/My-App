import random
import streamlit as st

st.set_page_config(
    page_title='운빨망겜',
    page_icon='🎲',
    layout='wide'
)

# 뽑기 결과 리스트
draw_dict = {
    "다이아몬드" : {
        "path": "https://i.namu.wiki/i/gyOaIJvqU66Hx3jpmESiPFzx7Kqj45EtYKixeFi2GGxbcHmheQtDFx7m8GHl_LP5-6VGLwWsKJzROtcp8FP_Yg.webp",
        "prob": 1
    },
    "루비" : {
        "path": "https://cdn.hankyung.com/photo/202204/01.29809496.1.jpg",
        "prob": 5
    },
}

# 뽑기 박스 생성
draw_box = []
for item, info in draw_dict.items():
    box = [[item, info]] * info['prob']
    draw_box += box

# 뽑기 통계
inven_box = {}
for item, info in draw_dict.items():
    inven_box[item] = {
        'count': 0,
        'path': info['path'],
        'name': item
    }

if 'inven_box' not in st.session_state:
    st.session_state['inven_box'] = inven_box


# 페이지 제목
st.markdown("## ☢ 보석뽑기")

# 뽑기 버튼
draw_btn = st.button("📈 뽑기!!")

# 열(Column) 나누기
col1, col2 = st.columns(2)

result = None
# 첫번째 열(col1) : 뽑기 결과
with col1:
    if draw_btn:
        result = random.choice(draw_box)
        result_html = f"""
            <div style="
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                width: 500px;
                height: 500px;
                border: 3px solid #2980b9;
                border-radius: 50%;
            ">
                <b>{result[0]}</b>
                <img src={result[1]["path"]} width="150px" height="150px">
            </div>
        """

        st.markdown(result_html, unsafe_allow_html=True)

# 두번째 열(col2) : 뽑기 통계
with col2:
    if result:
        st.session_state['inven_box'][result[0]]['count'] += 1
    
    item_html = ""
    for item, info in st.session_state['inven_box'].items():
        item_html += f"""
            <div style="
                border: 2px solid blue;
                border-radius: 10px;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                width: 150px;
                height: 150px;
                background: #aaa;
                font-weight: 800;
            ">
                <img 
                style="
                    width: 100px;
                    height: 100px;
                    margin-bottom: 10px;
                "
                src={info['path']}>
                <span>{item}({info['count']})</span>
            </div>"""
        

    inven_html = f"""
        <div style="
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
        ">{item_html}</div>
    """

    st.markdown(inven_html, unsafe_allow_html=True)