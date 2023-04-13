import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Image and Video App")

    menu = ["Image", "Video"]
    choice = st.sidebar.selectbox("Select a section", menu)

    if choice == "Image":
        image_upload = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        use_camera = st.checkbox("Use camera")

        if use_camera:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            if ret:
                st.image(frame, caption="Captured Image")
                cap.release()
            else:
                st.warning("Unable to capture image from camera")

        if image_upload:
            image = np.array(image.open(image_upload))
            st.image(image, caption="Uploaded Image")

        caption = st.text_input("Enter a caption for the image")

    elif choice == "Video":
        video_upload = st.file_uploader("Upload a video", type=["mp4"])
        use_camera = st.checkbox("Use camera")

        if use_camera:
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            if ret:
                st.video(frame, caption="Captured Video")
                cap.release()
            else:
                st.warning("Unable to capture video from camera")

        if video_upload:
            st.video(video_upload, caption="Uploaded Video")

        caption = st.text_input("Enter a caption for the video")

    if caption:
        st.write("Caption:", caption)

if __name__ == "__main__":
    main()
