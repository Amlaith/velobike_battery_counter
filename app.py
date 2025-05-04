import io
import streamlit as st
from PIL import Image
from image_processing import remove_green, bike_screenshot_to_string

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True, type=["jpg", "jpeg", "png"]
)
for uploaded_file in uploaded_files:
    imagefile = io.BytesIO(uploaded_file.read())
    im = Image.open(imagefile)
    # Do something with im
    st.image(im)

