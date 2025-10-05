#주어진 주제에 따라 설명을 요청하는 함수
from openai import OpenAI
from dotenv import load_dotenv
from typing import List

prompt_template = "주제 {topic}에 대해 짧은 설명을 해주세요."
load_dotenv()
client = OpenAI()

def call_chat_model(messages: List[dict]):
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages,
    )
    return response.choices[0].message.content

def invoke_chain(topic : str):
    prompt_value = prompt_template.format(topic = topic)
    messages = [{"role" : "user", "content" : prompt_value}]
    answer = call_chat_model(messages)
    print(answer)
    return answer
    
invoke_chain("LG트윈스")