import streamlit as st
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

st.title("Voice-to-Voice Translator")

# Language selection
input_lang = st.selectbox("Select Input Language", ["en", "es", "fr"])
output_lang = st.selectbox("Select Output Language", ["en", "es", "fr"])

# Initialize recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

if st.button("Start Speaking"):
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language=input_lang)
            st.write(f"Recognized: {text}")

            # Translate
            translated_text = translator.translate(text, src=input_lang, dest=output_lang).text
            st.write(f"Translated: {translated_text}")

            # Convert to speech
            tts = gTTS(translated_text, lang=output_lang)
            tts.save("output.mp3")
            st.audio("output.mp3", format="audio/mp3")

        except Exception as e:
            st.write(f"Error: {str(e)}")
