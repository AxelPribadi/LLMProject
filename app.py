import streamlit as st

from model import predict_text

st.set_page_config(page_title="XLP AI Detector", page_icon=":rocket:")
st.markdown("<h1 style='text-align: center;'>AI Content Detector</h1>", unsafe_allow_html=True)

user_input = st.text_area("Enter Text", placeholder="Enter your text here...")

if st.button("Classify"):
    pred, score = predict_text(user_input)

    pred = "Human Text" if pred == 0 else "AI Text" 
    score = round(score *100, 2) 

    st.write("Result:", pred)
    st.write("Probabilty:", str(score), "%")



