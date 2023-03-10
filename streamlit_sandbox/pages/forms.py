import streamlit as st
import datetime

st.title('入力フォーム')

st.caption('入力してね')
with st.form(key='profile_form'):
    name = st.text_input('名前')

    # submit 処理を擬似的に実装
    # submit_btn(送信) をクリックすることで入力フォームで入力した情報が表示されます
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'こんにちは {name} さん')
