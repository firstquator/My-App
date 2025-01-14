# https://docs.streamlit.io/develop/api-reference
import streamlit as st


pages = {
    "MENU": [
        st.Page("./navigations/up_and_down.py", title="🎮 UP & DOWN 게임"),
        st.Page("./navigations/lotto.py", title="📰 로또 번호 생성"),
    ]
}

page = st.navigation(pages)
page.run()