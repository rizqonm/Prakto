import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_KEY")

messages = [
    {"role": "system", "content": "Kamu adalah asisten AI yang ahli dalam menjelaskan konsep teknologi."},
    {"role": "user", "content": "Jelaskan tentang apa itu blockchain"}
]

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=messages,
        max_tokens=100,
        temperature=0.7
    )
    
    explanation = response['choices'][0]['message']['content']
    print("Penjelasan tentang Analisis Perancangan Sistem:")
    print(explanation)
except Exception as e:
    print("Terjadi kesalahan:", e)
