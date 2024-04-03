# web app or mobile app
# here i am creating a web app (front end) that will interact with the api

import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke",
       json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/poem/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    # streamlit framework 

st.title("LangChain Demo With LLAMA2 API")
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response( input_text))

if input_text:
    st.write(get_ollama_response( input_text))
