from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
   model_name: str
   model_provider: str
   system_prompt: str
   messages: List[str]
   allow_search: bool

from fastapi import FastAPI, Request

Allowed_model_providers = ["openai/gpt-oss-12b","mixtral-8x7b-32768","gpt-4o-mini","gpt-4o","gpt-4o-mini-32k","gpt-4o-mini-16k","gpt-4o-mini-8k","gpt-4o-mini-4k"]

app = FastAPI(title="Langraph AI Agent")
@app.post("/chat")
def chat_endpoint(request:RequestState):
    if request.model_provider not in Allowed_model_providers:
        return {"error": "Invalid model provider"}
