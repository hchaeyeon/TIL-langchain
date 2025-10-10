#생성된 설명을 영어로 번역하는 체인 추가
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
#오픈AI의 대규모 언어 모델 설정
model = ChatOpenAI(model= "gpt-4o-mini")

#프롬프트 템플릿 정의 : 주어진 주제에 대한 설명 요청
prompt = ChatPromptTemplate.from_template("{topic}에 대해 설명 해주세요.")

chain = prompt | model | StrOutputParser()

#"이 대답을 영어로 번역해 주세요" 라는 질문을 생성하는 프롬프트 템플릿 정의
analysis_prompt = ChatPromptTemplate.from_template("이 대답을 영어로 번역해 주세요 : {answer}")

#람다 함수를 사용한 체인 구성
composed_chain_with_lambda = (
    #이전에 정의된 체인(chain)을 사용하여 입력된 데이터를 받아옵니다.
    chain
    #입력된 데이터를 "answer" 키로 변환하는 람다 함수를 적용합니다.
    |(lambda input: {"answer": input})
    #"answer" 키를 가진 데이터를 영어로 번역하도록 프롬프트에 전달합니다.
    |analysis_prompt
    #프롬프트에서 생성된 요청을 모델에 전달하여 결과를 생성
    |model
    #모델에서 반환된 결과를 문자열로 파싱
    |StrOutputParser()
)

response = composed_chain_with_lambda.invoke({"topic" : "KBO"})

print(response)