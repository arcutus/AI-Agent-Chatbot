import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="wide",page_icon="🤖")
st.title("AI Chatbot Agents")
st.write("Create and Interact with AI agents using different models and providers.")

system_prompt = st.text_area("Define your AI Agent's System Prompt",height=70,placeholder="Type your system prompt here...")

MODEL_NAME_GROQ=["mixtral-8x7b-32768"]
MODEL_NAME_OPENAI=["openai/gpt-oss-20b","openai/gpt-oss-120b","gpt-4o-mini","gpt-4o"]

provider=st.radio("Select Model Provider",("groq","openai"))

if provider=="groq":
    selected_model=st.selectbox("Select Model",MODEL_NAME_GROQ)
elif provider=="openai":
    selected_model=st.selectbox("Select Model",MODEL_NAME_OPENAI)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter your query",height=70,placeholder="ask anything...")