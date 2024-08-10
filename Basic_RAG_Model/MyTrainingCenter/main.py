import streamlit as st
import langchain_helper

st.title("Institute Name Generator")

course = st.sidebar.selectbox("Pick a Subject", ("AIML", "Gen AI", "Big Data", "Java", "Python"))

if course:
    response = langchain_helper.generate_Institute_name(course)
    st.header(response['Institute_name'].strip())
    Subjects = response['subject'].strip().split(",")
    st.write("**Course Name**")
    for item in Subjects:
        st.write("-", item)

