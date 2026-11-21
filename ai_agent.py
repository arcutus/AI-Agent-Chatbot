import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY= os.environ.get("OPENAI_API_KEY")

#seting up LLm and Tools
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

def get_response_from_agent(llm_id,query,allow_search,system_prompt,provider):
    if provider == "groq":
        groq_llm = ChatGroq(model=llm_id)
        
    elif provider == "openai":
        from langchain.chat_models import ChatOpenAI
        openai_llm = ChatOpenAI(model_name=llm_id, openai_api_key=OPENAI_API_KEY)
        search_tool = TavilySearch(max_results=3)if allow_search else{}
        agent = create_agent(
            model=openai_llm,
            tools=[search_tool] if allow_search else [],
            system_prompt=system_prompt
        )
    else:
        raise ValueError("Invalid model provider")

    response = agent.invoke({"messages": [("user", query)]})
    return response["messages"][-1].content
   

groq_llm = ChatGroq(model="openai/gpt-oss-12b")
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
state={"messages":query}
response = agent.invoke(state)
messages = response.get("messages")
ai_messages =[messages.content for messages in messages if isinstance(message, AIMessage)]
messages[-1] if ai_messages else "No response from the agent."

#query=input("Enter your query: ")
response = agent.invoke({"messages": [("user", query)]})
print(response["messages"][-1].content)
