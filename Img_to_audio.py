import streamlit as st
import cv2
import numpy as np
from gtts import gTTS
import os
from IPython.display import Audio
import pytesseract
from PIL import Image

page_bg_img = '''
    <style>
    body {
    background-image: url("https://www.netpremacy.com/wp-content/uploads/2018/09/Background-website-01.jpg");
    background-size: cover;
    }
    </style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Image-Text-Speech Converter for Visually Impaired")
st.markdown("This application here is used to retrieve the text from Selected Image and then convert that text to  Audio. This is a very helpful tool for Visually impaired people.")
st.markdown("Now Don't wait for your audiobook to release, Create your own using this application")

#live capture of image
st.markdown("## Click on the Browse button to select the image 📷")
uploaded_file = st.file_uploader("Choose an image file", type=("jpg","png"))
st.markdown("## Click on the button below to convert the image to audio")
if st.button("Convert Image to Audio"):
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        st.image(opencv_image, width=600, channels="BGR")
        pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        text=pytesseract.image_to_string(opencv_image)
        file1 = open("MyFile.txt","w+")
        file1.write(text)
        file1.close()
        st.markdown("## Text retrieved from Image")
        st.markdown(text)
        tts = gTTS(text) #Provide the string to convert to speech
        tts.save('1.wav') #save the string converted to speech as a .wav file
        sound_file = '1.wav'
        st.markdown("## Click on play button to play converted audio file")
        st.audio(sound_file, format='audio/wav')
    else:
        st.markdown("### Please select an image to convert!!!")
