import streamlit as st
page_bg_img = '''<style>
.stApp {
    background-image: url("https://picsum.photos/1080/768");
    background-size: cover;
}
</style>'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("My Webpage")
#tab1,tab2 = st.tabs(['Left', 'Right'])
st.sidebar.header("with")
st.sidebar.subheader("Beautiful Background Image")
with st.expander('see my video?'):
    c = st.container()
    video_file = open('star.mp4', 'rb')
    video_bytes = video_file.read()
    c.write('This is my darksky video.')
    c.video(video_bytes)
    c.write('This is my darksky image.')
    c.image('https://picsum.photos/650/300')