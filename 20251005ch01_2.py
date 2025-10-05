from openai import OpenAI
from dotenv import load_dotenv
from typing import List

load_dotenv()
client = OpenAI()

#요청에 사용할 프롬프트 템플릿 정의
prompt_template = "주제 {topic}에 대해 짧은 설명을 해주세요."

#메시지를 보내고 모델의 응답을 받는 함수
def call_chat_model(messages: List[dict]):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages,
    )
    return response.choices[0].message.content


# 프롬프트 메시지 생성
topic = "더블딥"
messages = [
    {"role": "user", "content": prompt_template.format(topic=topic)}
]

# 함수 호출 & 결과 저장
answer = call_chat_model(messages)

# 결과 출력
print("GPT 응답:", answer)