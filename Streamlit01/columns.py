import streamlit as st
page_bg_img = '''<style>
.stApp {
    background-image: url("https://picsum.photos/1080/768");
    background-size: cover;
}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("My Webpage")
left,right = st.columns(2)
left.header("with")
left.subheader("Beautiful Background Image")
video_file = open('star.mp4', 'rb')
video_bytes = video_file.read()
right.video(video_bytes)