import streamlit as st
import requests


cols = st.columns([0.5,4,0.5])


with cols[1]:
    st.title("URL Shortener")
    st.caption("Make your links more manageable, trackable, and shareable with our advanced URL shortening service.")
    st.divider()
    st.write('') 
    long_url = st.text_input('Paste your long URL here', placeholder='URL here')
    is_clicked = st.button('Shorten!', use_container_width=True, type='primary')
    
    if is_clicked:
        res = requests.post(f'http://127.0.0.1:8000/shorten?long_url={long_url}')
        if res.status_code == 200:
            st.toast('Success')
            res = res.json()
            st.link_button(f'{res}', url=res)