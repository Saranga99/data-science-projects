import json
import streamlit as st
import requests
import time

get_content_url='http://127.0.0.1:8000/questionContent/'
get_answers_url='http://127.0.0.1:8000/questionAnswering/'
st.set_page_config(page_title="Question Answering",layout="wide",
     initial_sidebar_state="expanded",)

st.markdown("# parkinson's disease question answering")

def get_context():
    st.markdown("## Get Question Context")
    txt_question=st.text_input("Question","How do I toilet train my child as he keeps wetting himself?")
    btn_get_ans=st.button("Get Answers")

    if btn_get_ans:
        session = requests.Session()
        try:
            data ={
                    "message":txt_question
                }
            with st.spinner('Finding Answers...'):
                result = session.post(get_content_url,data=json.dumps(data))
                time.sleep(5)
            st.success('Done!')
            data_json = json.loads(result.text)
            st.write(data_json)
        except Exception:
            st.write("Error")
    

def get_answers():
    st.markdown("## Get Answers")
    txt_question=st.text_input("Question","My child has a hard time drinking from the bottle, what can I do?")
    btn_get_ans=st.button("Get Answers")

    if btn_get_ans:
        session = requests.Session()
        try:
            data ={
                    "message":txt_question
                }
            with st.spinner('Finding Answers...'):
                result = session.post(get_answers_url,data=json.dumps(data))
                time.sleep(5)
            st.success('Done!')
            data_json = json.loads(result.text)
            st.write(data_json)
            
        except Exception:
            st.write("Error")




page_names_to_funcs = {
    "Get Context": get_context,
    "Get Answers": get_answers
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()