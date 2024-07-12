import streamlit as st
import sounddevice as sd  
import numpy as np  
from io import BytesIO  
import requests  
import os

  
# Function to record audio  
def record_audio(duration=5, fs=44100):  
    st.write("Recording...")  
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)  
    sd.wait()  # Wait until recording is finished  
    st.write("Recording finished")  
    audio = np.int16(audio * 32767)  # Convert to 16-bit PCM format  
    byte_io = BytesIO()  
    byte_io.write(audio.tobytes())  
    byte_io.seek(0)  
    return byte_io  
  
# Function to play audio  
def play_audio(audio_bytes):  
    st.audio(audio_bytes, format='audio/wav')  
  
# Function to convert text to speech (using a placeholder API)  
def text_to_speech(text):  
    url = "https://api.fake-text-to-speech.com/convert"  
    params = {'text': text}  
    response = requests.get(url, params=params)  
    audio_data = response.content  
    return audio_data  
  
# Streamlit app layout  
st.title("Streamlit Chatbot Interface")  
  
# Text input  
user_input = st.text_input("Enter your message:")  
  
# Camera input  
image = st.camera_input("Capture an image from your webcam:")  
  
if image:  
    st.image(image, caption="Captured Image", use_column_width=True)  
  
# Microphone input  
if st.button("Record Audio"):  
    audio_bytes = record_audio()  
    if audio_bytes:  
        play_audio(audio_bytes)  
  
# Process user input and generate responses  
if user_input:  
    response1 = f"Echo: {user_input}"  
    response2 = f"Reversed: {user_input[::-1]}"  
    st.text_area("Response 1:", response1, height=100)  
    st.text_area("Response 2:", response2, height=100)  
      
    # Convert response1 to speech  
    audio_response = text_to_speech(response1)  
    st.audio(audio_response, format='audio/wav')  
  
# Note: The text_to_speech function uses a placeholder API. Replace the URL with an actual TTS API endpoint.  
