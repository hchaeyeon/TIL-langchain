#라이브러리 불러오기
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
#오픈AI의 대규모 언어 모델 설정
model = ChatOpenAI(model= "gpt-4o-mini")

#프롬프트 템플릿 정의 : 주어진 주제에 대한 설명 요청
prompt = ChatPromptTemplate.from_template("주제 {topic}에 대해 짧은 설명을 해주세요.")

#출력 파서 정의 : AI 메시지의 출력 내용을 추출
parser = StrOutputParser()

#프롬프트, 모델, 출력 파서를 체인으로 연결
chain = prompt | model | parser

#응답 호출
response = chain.invoke({"topic" : "더블딥"})

#주어진 주제 리스트에 대한 응답을 배치로 출력
responses = chain.batch([{"topic" : "더블딥"}, {"topic" : "인플레이션"}])

print(response)
print(responses)