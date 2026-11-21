import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY= os.environ.get("OPENAI_API_KEY")

#seting up LLm and Tools
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

groq_llm = ChatGroq(model="openai/gpt-oss-120b")


search_tool = TavilySearch(max_results=3)

#setting up the agent
from langchain.agents import create_agent

system_prompt = "You are a helpful assistant that can answer questions using the tools provided. Use the tools to find information and provide accurate answers. Act as an AI chatbot who is smart and friendly."

agent = create_agent(
    model=groq_llm,
    tools=[search_tool],
    system_prompt=system_prompt
)

query=input("Enter your query: ")
response = agent.invoke({"messages": [("user", query)]})
print(response["messages"][-1].content)
