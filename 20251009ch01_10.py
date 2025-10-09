from openai import OpenAI
from dotenv import load_dotenv
import os, sys

load_dotenv()
print("PY:", sys.executable)
print("API 키 감지됨:", bool(os.getenv("OPENAI_API_KEY")))

client = OpenAI()
resp = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "안녕하세요!"}],
)
print(resp.choices[0].message.content)

