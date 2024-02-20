import streamlit as st
h = st.header('my web')
s = st.subheader('เว็บไซน์ส่วนตัว')
p = st.write('เว็บถูกสร้างแบบรันไม่ได้')
banner = st.image('https://picsum.photos/800/250')
text = st.text_input('prompt: ')
if text:
    st.write(f'กำลังจะสร้างภาพ...."{text}')
    b = st.button('จะไปต่อหรือ')
