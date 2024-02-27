import streamlit as st
page_bg_img = '''<style>
.stApp {
    background-image: url("https://picsum.photos/1080/768");
    background-size: cover;
}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("My Webpage")
tab1,tab2 = st.tabs(['Left', 'Right'])
tab1.header("with")
tab1.subheader("Beautiful Background Image")

video_file = open('star.mp4', 'rb')
video_bytes = video_file.read()
tab2.video(video_bytes)