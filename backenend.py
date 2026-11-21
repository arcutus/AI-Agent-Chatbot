from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import get_response_from_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

Allowed_model_providers = [
    "openai/gpt-oss-20b",
    "openai/gpt-oss-120b",
    "mixtral-8x7b-32768",
    "gpt-4o-mini",
    "gpt-4o"
]

app = FastAPI(title="Langgraph AI Agent")

@app.post("/chat")
def chat_endpoint(request: RequestState):
    if request.model_name not in Allowed_model_providers:
        return {"error": "Invalid model provider"}

    response = get_response_from_agent(
        llm_id=request.model_name,
        query=request.messages[-1],
        allow_search=request.allow_search,
        system_prompt=request.system_prompt,
        provider=request.model_provider
    )
    return {"response": response}
