import streamlit as st
from langchain import OpenAI
from llama_index import GPTSimpleVectorIndex, LLMPredictor

llm_predictor = LLMPredictor(llm=OpenAI(
    temperature=0, model_name="gpt-3.5-turbo"))

st.title('myGPT')

with st.form(key='talk'):
    prompt = st.text_area("お話しましょう")
    submit_btn = st.form_submit_button('送信')

if submit_btn:
    vector_index = GPTSimpleVectorIndex.load_from_disk(
        save_path="index.json", llm_predictor=llm_predictor
    )
    answer = vector_index.query(
        prompt
    )
    st.markdown(answer)
