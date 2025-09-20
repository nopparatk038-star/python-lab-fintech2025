import streamlit as st

name = st.text_input("name")
if st.button("set name") :
    st.success(f'Settings saved for {name}!')
    st.session_state['username']=name