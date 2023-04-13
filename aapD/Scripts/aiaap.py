import streamlit as st
from PIL import Image
import cv2
# Add a navigation menu
st.sidebar.title('Navigation')
menu = ['Image', 'Video']
choice = st.sidebar.selectbox('Select an option', menu)
# Allow users to upload files
if choice == 'Image':
    st.subheader('Upload an image')
    file = st.file_uploader('Choose an image', type=['jpg', 'jpeg', 'png'])
else:
    st.subheader('Upload a video')
    file = st.file_uploader('Choose a video', type=['mp4'])
# Display the selected file
if file is not None:
    if choice == 'Image':
        image = Image.open(file)
        st.image(image, caption='Uploaded Image')
    else:
        video = file.read()
        st.video(video, caption='Uploaded Video')
    
    # Add a caption
    caption = st.text_input('Enter a caption')
    st.write('Caption:', caption)
