import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 AI Language Translator")

source = st.selectbox(
    "Source Language",
    ["en", "hi", "te", "kn", "ta"]
)

target = st.selectbox(
    "Target Language",
    ["hi", "en", "te", "kn", "ta"]
)

text = st.text_area("Enter Text")

if st.button("Translate"):
    translated = GoogleTranslator(
        source=source
        target=target
    ).translate(text)

    st.success("Translation")
    st.write(translated)