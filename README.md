# Customer Complaint Summarizer API

A simple FastAPI backend that connects to GPT-4 to summarize customer messages and extract:
- Summary
- Category (e.g., Refund Issue)
- Urgency (e.g., High)
- Sentiment (e.g., Negative)

## Setup

- Works seamless on a ubuntu machine
```bash
git clone https://github.com/vitesh2002/oriserve.git
cd oriserve
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Add your OpenAI key at line 7 in main.py file inside double quotes.(Removed .env file for convenience)

## RUN

```bash
uvicorn main:app --reload
```

## Example Request

- Open a new terminal and run the below curl to test.
```bash
curl -X POST http://127.0.0.1:8000/summarize      -H "Content-Type: application/json"      -d '{"message": "I’ve been waiting 3 days for my refund and your support hasn’t replied. This is really frustrating."}'
```

## Example Response

```bash
{
  "summary": "Customer is frustrated about the delay in receiving a refund and lack of response from support.",
  "category": "Refund Issue",
  "urgency": "High",
  "sentiment": "Negative"
}
```
