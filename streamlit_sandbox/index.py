import streamlit as st
import openai

st.title('myGPT')

with st.form(key='talk'):
    prompt = st.text_area("お話しましょう")
    submit_btn = st.form_submit_button('送信')

if submit_btn:
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": prompt},
        ]
    )
    response = ""
    for cho in completion.choices:
        response += cho.message.content
    st.markdown(response)