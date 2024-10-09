import requests
import streamlit as st

def get_llama_response(input_text):
    response= requests.post("http://localhost:8000/essay/invoke", json = {'input':{'topic': input_text}})
    return response.json()['output']

def get_llama2_response(input_text):
    response= requests.post("http://localhost:8000/poem/invoke", json = {'input':{'topic': input_text}})
    return response.json()['output']



st.title("momo and onnu bot")
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write an poem on")

if input_text:
    st.write(get_llama_response(input_text))
if input_text1:
    st.write(get_llama2_response(input_text1))
