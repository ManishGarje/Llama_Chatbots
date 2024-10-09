from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn 
import os
from langchain_community.llms import Ollama

from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

app =FastAPI(
    title ='Langchain Server',
    version = '1.0',
    description = 'simple api server'
)


llm1 = Ollama(model  =  'llama3.2')
llm2 = Ollama(model ="moondream")

prompt1 = ChatPromptTemplate.from_template("write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("write me an poem about {topic} with 100 words")

add_routes(
    app,
    prompt1|llm1,
    path = "/essay"
)
add_routes(
    app,
    prompt2|llm2,
    path = "/poem"
)

if __name__ == "__main__":
    uvicorn.run(app,host = "localhost", port = 8000)