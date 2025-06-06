from fastapi import FastAPI, Request
from pydantic import BaseModel
from openai import OpenAI
import os
import json

client = OpenAI(api_key="your_api_key")

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/summarize")
async def summarize(msg: Message):
    prompt = f"""
    Analyze the following customer message and respond in JSON with:
    - A brief summary
    - Category (Refund Issue, Delay, Account Access, etc.)
    - Urgency (Low, Medium, High)
    - Sentiment (Positive, Neutral, Negative)

    Message: "{msg.message}"

    Return only JSON.
    """

    response = client.chat.completions.create(
        model="gpt-4",  
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    result = response.choices[0].message.content.strip()
    result = result.replace("```json", "").replace("```", "").strip()
    return json.loads(result)
