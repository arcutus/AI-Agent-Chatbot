# AI Agent Chatbot

A lightweight AI chatbot built with Streamlit, FastAPI, and LangChain. Choose a Groq or OpenAI model, provide a custom system prompt, and optionally let the agent search the web with Tavily.

## Features

- Streamlit interface for sending a prompt to the agent
- FastAPI `/chat` endpoint
- Groq models: `openai/gpt-oss-20b` and `openai/gpt-oss-120b`
- OpenAI models: `gpt-4o-mini` and `gpt-4o`
- Optional web search through Tavily (up to three results)
- Custom system prompt, with a helpful default when left blank
- Command-line prompt mode in `ai_agent.py`

## Project files

- `frontdend.py` — Streamlit user interface (filename as provided)
- `backend.py` — FastAPI application and `/chat` route
- `ai_agent.py` — LangChain agent setup for Groq/OpenAI and optional Tavily search
- `Pipfile` / `Pipfile.lock` — Pipenv dependency definitions

## Requirements

- Python 3.14 (as specified in the Pipfile)
- API key for the model provider you plan to use
- Tavily API key if web search is enabled

## Setup

Clone the repository and enter its directory:

```bash
git clone https://github.com/arcutus/AI-Agent-Chatbot.git
cd AI-Agent-Chatbot
```

Create and activate a virtual environment, then install the project dependencies. With Pipenv:

```bash
pip install pipenv
pipenv install
pipenv shell
```

Create a `.env` file in the project directory and add the keys for the providers you intend to use:

```env
GROQ_API_KEY=your_groq_api_key
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Keep `.env` private; do not commit API keys to source control. Only the model provider key you select is needed. `TAVILY_API_KEY` is needed when enabling web search.

## Run the app

Start the API in one terminal:

```bash
python backend.py
```

The API listens locally at `http://127.0.0.1:8000`. In another terminal, launch the Streamlit interface:

```bash
streamlit run frontdend.py
```

Open the local URL printed by Streamlit in your browser. Select a provider and model, optionally enter a system prompt and enable web search, then submit a query.

## API

`POST /chat` accepts JSON in this form:

```json
{
  "model_name": "openai/gpt-oss-20b",
  "model_provider": "groq",
  "system_prompt": "You are a helpful assistant.",
  "messages": ["What is LangChain?"],
  "allow_search": false
}
```

A successful response has this form:

```json
{
  "response": "..."
}
```

The `model_name` must be one of the four models listed in the Features section. `model_provider` must be `groq` or `openai`, and should match the selected model. When web search is enabled, the agent uses Tavily and retrieves up to three results.

## Run the agent from the command line

`ai_agent.py` also contains a simple interactive prompt mode. It uses the Groq `openai/gpt-oss-20b` model with Tavily search enabled:

```bash
python ai_agent.py
```

## License

No license file is currently included in the repository. Check with the repository owner before reusing or redistributing the code.
