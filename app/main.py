from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.utils.auth import is_valid_key
from app.classifier import get_intent

app = FastAPI()

class IntentRequest(BaseModel):
    key: str
    text: str
    guid: str

class IntentResponse(BaseModel):
    intent: str
    text: str
    guid: str

@app.post("/predict-intent", response_model=IntentResponse)
def predict_intent(request: IntentRequest):
    if not is_valid_key(request.key):
        raise HTTPException(status_code=401, detail="Invalid API key")

    intent = get_intent(request.text)

    return IntentResponse(
        intent=intent,
        text=request.text,
        guid=request.guid
    )
