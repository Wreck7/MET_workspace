import streamlit as st
from api import register

col = st.columns([2,6,2])

with col[1]:
    st.header('Register')
    email = st.text_input('Email', placeholder='Enter your email')
    username = st.text_input('Username', placeholder='Enter your username')
    name = st.text_input('Fullname', placeholder='Enter your fullname')
    age = st.text_input('Age', placeholder='Enter your age')
    gender = st.radio('Gender',options=['Male', 'Female'], horizontal=True)
    password = st.text_input('Password',placeholder='Set a password',type='password')
    is_agree = st.checkbox('Agree terms & conditions')
    is_done = st.button('Register',use_container_width=True, type='primary')
    if is_done:
        if email and username and name and age and gender and password and is_agree:
            data = register(username, email, name, age, password, gender)
            if data:
                st.toast('Register successful')
            else:
                st.toast('User already exist')
        else:
            st.toast('Fill all the fields')

