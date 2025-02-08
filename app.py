#https://docs.streamlit.io/develop/api-reference
import streamlit as st
pages={
    'Menu':[
        st.Page('./navigations/home.py',title='💒 Home'),
        st.Page('./navigations/up&down.py',title='👍👎 up&down'),
        st.Page('./navigations/lotto.py',title='💵 Lottery'),
        st.Page('./navigations/gacha.py',title='🎲 Gacha Game'),
    ],
}

page = st.navigation(pages)
page.run()