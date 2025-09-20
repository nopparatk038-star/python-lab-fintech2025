import pandas as pd
import streamlit as st

st.title("Dashboard")
st.write("This application is about disply product sales")

if 'username' in st.session_state:
    st.write(f'Hello ! {st.session_state['username']}')
else:
    st.info("Please register at setting page.")


upload_file = st.file_uploader("Choose a csv file", type="csv")

if upload_file is None:
    st.write("please upload csv file.")

else:

    data = pd.read_csv("products.csv")


    col1, col2, col3 = st.columns(3)
    with col1 :
        st.metric("Sales", "1,200", "12%")
    with col2 :
        st.metric("Revenue", "2,200", "5%")
    with col3 :
        st.metric("Margin", "200", "3%")

    name = st.text_input("name")
    st.write(name)



    st.line_chart(data['sales'])


    if st.checkbox("show table"):
        st.header("Sales table")
        st.subheader("This is a sales table")
        st.write(data)


