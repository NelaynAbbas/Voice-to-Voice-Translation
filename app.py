import streamlit as st
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
import os

st.title("Healthcare Translation Web App")

# Language selection
input_lang = st.selectbox("Select Input Language", ["en", "es", "fr", "de", "zh-cn"])
output_lang = st.selectbox("Select Output Language", ["en", "es", "fr", "de", "zh-cn"])

# Initialize Translator
translator = Translator()

# Speech recognition
recognizer = sr.Recognizer()
mic = sr.Microphone()

if st.button("Start Speaking"):
    with mic as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            # Convert Speech to Text
            text = recognizer.recognize_google(audio, language=input_lang)
            st.write(f"Recognized: {text}")

            # Translate with Google Translate API
            translated_text = translator.translate(text, src=input_lang, dest=output_lang).text
            st.write(f"Translated: {translated_text}")

            # Convert Translated Text to Speech
            tts = gTTS(translated_text, lang=output_lang)
            tts.save("output.mp3")
            st.audio("output.mp3", format="audio/mp3")
        
        except Exception as e:
            st.write(f"Error: {str(e)}")
