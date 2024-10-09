#from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ["LANGCHAIN_TRACING_V2"] = 'true'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

##prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "YOu are a helpful assistant. Please response to the queries")
        ("user","Question:{question}")
    ]
)

st.title("ManishBOT")
input_text = st.text_input("Search the topic u want")

#openAi llm
llm = ChatOpenAI(model = 'gpt-3.5-turbo')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
