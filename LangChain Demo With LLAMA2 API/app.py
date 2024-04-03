# responsible for creating all the api's

from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("openai_api_key")

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API Server"
)

add_routes(
    app,
    ChatOpenAI(), #model i will use
    path="/openai" #path

)
# models
model = ChatOpenAI() #1 model
llm = Ollama(model="llama2") #2 model

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words") # interacts with openai api : ChatOpenAI()
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words") # interacts with open source model : llm model

add_routes(
    app,
    prompt1 | model,
    path="/essay" #this path is responsible in interacting with the openai api and it is donatied by /essay

)

add_routes(
    app,
    prompt2 | llm,
    path="/poem" #this path is responsible in interacting with the llm and it is donatied by /poem

)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000) #this app you can run it in any server
