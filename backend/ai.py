# OpenAI para análise preditiva 
import openai
from backend.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def analyze_lead(data):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Analise o seguinte lead: {data}",
        max_tokens=50
    )
    return response["choices"][0]["text"]