import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Setting up LLM and Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain_core.messages import AIMessage
from langchain.agents import create_agent


def get_response_from_agent(llm_id, query, allow_search, system_prompt, provider):
    tools = [TavilySearch(max_results=3)] if allow_search else []

    prompt = system_prompt.strip() if system_prompt and system_prompt.strip() else (
        "You are a helpful assistant that can answer questions using the tools provided. "
        "Use the tools to find information and provide accurate answers. "
        "Act as an AI chatbot who is smart and friendly."
    )

    if provider == "groq":
        llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY)
    elif provider == "openai":
        llm = ChatOpenAI(model=llm_id, api_key=OPENAI_API_KEY)
    else:
        raise ValueError(f"Invalid model provider: {provider}")

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=prompt
    )

    response = agent.invoke({"messages": [("user", query)]})
    return response["messages"][-1].content


if __name__ == "__main__":
    groq_llm = ChatGroq(model="openai/gpt-oss-20b", api_key=GROQ_API_KEY)
    search_tool = TavilySearch(max_results=3)

    default_system_prompt = (
        "You are a helpful assistant that can answer questions using the tools provided. "
        "Use the tools to find information and provide accurate answers. "
        "Act as an AI chatbot who is smart and friendly."
    )

    agent = create_agent(
        model=groq_llm,
        tools=[search_tool],
        system_prompt=default_system_prompt
    )

    query = input("Enter your query: ")
    response = agent.invoke({"messages": [("user", query)]})
    messages = response.get("messages", [])
    ai_messages = [m.content for m in messages if isinstance(m, AIMessage)]
    if ai_messages:
        print(ai_messages[-1])
    else:
        print("No response from the agent.")
