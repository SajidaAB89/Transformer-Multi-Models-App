import json
import time

import streamlit as st
from streamlit_lottie import st_lottie
from transformers import pipeline


def app():
    st.title("Sentiment Analysis Model 😊")
    st.write("This model can analyze your sentiment based on provided context.")

    def get(path: str):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    path = get("./senti.json")

    st_lottie(
        path,
        speed=1,
        width=300,
        height=300,
        key="initial",
    )

    nlp = pipeline(
        task ="sentiment-analysis",
        model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    )

    statement = st.text_input("Enter your statement")
    if statement.strip() == "":
        st.warning("Please enter some text")
    elif st.button("Analyze"):
        with st.spinner("Wait for it..."):
            time.sleep(5)
            st.success("Done!")
    else:
        result = nlp(statement)[0]
        emoji = "😊" if result["label"] == "POSITIVE" else "😔"
        st.success(f"Sentiment: {result['label']} {emoji}")
        st.write(f"Confidence: {(result['score']*100):.2f}%")
      