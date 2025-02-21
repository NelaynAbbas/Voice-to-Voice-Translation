import streamlit as st
import googletrans
from googletrans import Translator
from gtts import gTTS
import os

st.title("Voice-to-Voice Translator")

# Language selection
input_lang = st.selectbox("Select Input Language", ["en", "es", "fr"])
output_lang = st.selectbox("Select Output Language", ["en", "es", "fr"])

translator = Translator()

# Audio Upload
uploaded_audio = st.file_uploader("Upload an audio file", type=["wav", "mp3"])

if uploaded_audio:
    st.audio(uploaded_audio, format="audio/wav")

    # Recognize speech (using Google Web Speech API)
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    
    with sr.AudioFile(uploaded_audio) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language=input_lang)
            st.write(f"Recognized Text: {text}")

            # Translate text
            translated_text = translator.translate(text, dest=output_lang).text
            st.write(f"Translated Text: {translated_text}")

            # Convert translation to speech
            tts = gTTS(translated_text, lang=output_lang)
            tts.save("output.mp3")
            st.audio("output.mp3", format="audio/mp3")

        except Exception as e:
            st.write(f"Error: {str(e)}")
