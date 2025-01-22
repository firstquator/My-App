import streamlit as st
import random

#home 웹 환경 설정
st.set_page_config(
    page_title='app home',
    page_icon='💒'
)


#이미지 주소 모음
img_path_box= {
    '무량공처':'https://mblogthumb-phinf.pstatic.net/MjAyNDA1MzBfMTY0/MDAxNzE3MDUxMjA2OTM2.j1bIwtYL4UtyIcqNHO_GyttzJE4dr3YN0yjao61l3rEg.gG93WFcGXRrCopcm-FswhuI1ZmqSb6zougbK50QpBr8g.GIF/%EB%AC%B4%EB%9F%89%EA%B3%B5%EC%B2%98_2.gif?type=w800',
    '복마어주자':'https://media.tenor.com/6sjiP4mArJwAAAAM/jujutsu-kaisen-%EC%A3%BC%EC%88%A0%ED%9A%8C%EC%A0%84.gif',
    '죠고':'https://blog.kakaocdn.net/dn/rRPnr/btqNq1dc2Xv/CRrCrMub6i3rUtY6rxyi2k/img.gif'
}

#----------------------------------------------
st.markdown('## My home')

gen_image_btn=st.button('💒 렌덤 이미지 생성')

if gen_image_btn:
    path_list=list(img_path_box.values())
    img_path=random.choice(path_list)
    st.image(img_path)