
import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

from model import predict_text


# model_path = "./local_model/"

# model = AutoModelForSequenceClassification.from_pretrained(model_path)
# tokenizer = AutoTokenizer.from_pretrained(model_path)

# classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)


# st.set_page_config(page_title="XLP AI Detector", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

st.set_page_config(page_title="XLP AI Detector", page_icon=":rocket:")
st.markdown("<h1 style='text-align: center;'>AI Content Detector</h1>", unsafe_allow_html=True)



user_input = st.text_area("Enter Text", placeholder="Enter your text here...")


if st.button("Classify"):
    # result = classifier(user_input, truncation=True, max_length=512)
    pred, score = predict_text(user_input)

    st.write("Result:", pred)
    st.write("Probabilty:", score)



