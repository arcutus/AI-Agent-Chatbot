import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="centered", page_icon="🤖")
st.title("AI Chatbot Agents")
st.write("Create and Interact with AI agents using different models and providers.")

system_prompt = st.text_area("Define your AI Agent's System Prompt", height=70, placeholder="Type your system prompt here...")

MODEL_NAME_GROQ = ["openai/gpt-oss-20b", "openai/gpt-oss-120b"]
MODEL_NAME_OPENAI = ["gpt-4o-mini", "gpt-4o"]

provider = st.radio("Select Model Provider", ("groq", "openai"))

if provider == "groq":
    selected_model = st.selectbox("Select Model", MODEL_NAME_GROQ)
elif provider == "openai":
    selected_model = st.selectbox("Select Model", MODEL_NAME_OPENAI)

allow_web_search = st.checkbox("Allow Web Search")

user_query = st.text_area("Enter your query", height=70, placeholder="ask anything...")

# Backend API URL
API_URL = "http://127.0.0.1:8000/chat"

if st.button("Ask Query"):
    if user_query.strip():
        import requests

        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        try:
            with st.spinner("Agent is thinking..."):
                response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(f"Error: {response_data['error']}")
                else:
                    st.subheader("Agent Response")
                    st.markdown(f"**Final Response:** {response_data.get('response')}")
            else:
                st.error(f"Backend Server Error ({response.status_code}): {response.text}")
        except requests.exceptions.ConnectionError:
            st.error("Could not connect to backend server. Make sure `python backend.py` is running on http://127.0.0.1:8000.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please enter a query before clicking 'Ask Query'.")
