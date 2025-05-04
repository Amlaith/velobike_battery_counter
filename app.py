import io
import streamlit as st
from PIL import Image
from image_processing import remove_green, bike_screenshot_to_string

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True, type=["jpg", "jpeg", "png"]
)

text = ""

for uploaded_file in uploaded_files:
    imagefile = io.BytesIO(uploaded_file.read())
    img = Image.open(imagefile)
    # st.image(im)
    img = remove_green(img)
    text += bike_screenshot_to_string(img)

st.write(text)



