#챗 프롬프트 템플릿 생성하기
#챗 프롬프트 템플릿 = 대화형 AI모델과 상호작용하는 데 필요한 메시지 시퀀스를 생성하는 구조
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatMessagePromptTemplate
from dotenv import load_dotenv

load_dotenv()

#챗 프롬프트 템플릿 정의 : 사용자와 시스템 간의 메시지 포함
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "당신은 유능한 금융 조언가입니다."),
    ("user", "주제{topic}에 대해 금융 관련 조언을 해주세요.")
])

result = prompt_template.invoke({"topic" : "주식"})
print(result)