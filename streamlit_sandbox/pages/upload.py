import streamlit as st
import os
from llama_index import GPTSimpleVectorIndex,  OpenAIEmbedding, SimpleDirectoryReader

st.title('ファイルのアップロード')
st.caption('ファイルのアップロード')

uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True)
if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        with open(os.path.join("./storage", uploaded_file.name), 'wb') as f:
            f.write(bytes_data)
    documents = SimpleDirectoryReader('./storage').load_data()
    embed_model = OpenAIEmbedding(model="text-embedding-ada-002")
    vector_index = GPTSimpleVectorIndex(
        documents=documents, embed_model=embed_model
    )
    vector_index.save_to_disk(save_path="index.json")

files = os.listdir("./storage")
for file in files:
    if file == ".gitignore":
        continue
    st.write(file)
