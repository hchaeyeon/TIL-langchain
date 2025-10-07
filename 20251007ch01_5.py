from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# .env 파일에서 OPENAI_API_KEY 불러오기
load_dotenv()

# LLM 모델 초기화(파라미터 설정)
llm = OpenAI(
    temperature=0.7, #온도 설정(0에서 1 사이의 값)
    max_tokens=100,  #최대 토큰 수 설정
    model_name="gpt-3.5-turbo-instruct" #사용할 모델 지정
)

# 프롬프트 입력 및 실행
prompt = "버블경제란 무엇인가요?"
response = llm.invoke(prompt)

print("🧠 모델 응답:")
print(response)