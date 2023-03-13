import streamlit as st
import os

st.title('ファイルのアップロード')
st.caption('ファイルのアップロード')

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    with open(os.path.join("./storage", uploaded_file.name), 'wb') as f:
        f.write(bytes_data)
