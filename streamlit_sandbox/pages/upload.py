import streamlit as st
import os
from llama_index import GPTSimpleVectorIndex,  OpenAIEmbedding, SimpleDirectoryReader

st.title('ファイルのアップロード')
st.caption('ファイルのアップロード')
if not os.path.exists('index.json'):
    embed_model = OpenAIEmbedding(model="text-embedding-ada-002")
    vector_index = GPTSimpleVectorIndex(
        documents=[], embed_model=embed_model
    )
    vector_index.save_to_disk(save_path="index.json")
uploaded_file = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=False)
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    with open(os.path.join("./storage", uploaded_file.name), 'wb') as f:
        f.write(bytes_data)
    documents = SimpleDirectoryReader('./storage').load_data()
    embed_model = OpenAIEmbedding(model="text-embedding-ada-002")
    vector_index = GPTSimpleVectorIndex.load_from_disk(
        save_path="index.json", embed_model=embed_model
    )
    for doc in documents:
        vector_index.insert(doc)
    vector_index.save_to_disk(save_path="index.json")

files = os.listdir("./storage")
for file in files:
    if file == ".gitignore":
        continue
    st.write(file)
