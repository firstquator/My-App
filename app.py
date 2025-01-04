import streamlit as st


pages = {
    "MENU": [
        st.Page("./navigations/up_and_down.py", title="🎮 UP & DOWN 게임")
    ]
}

page = st.navigation(pages)
page.run()