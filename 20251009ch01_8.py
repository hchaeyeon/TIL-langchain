#생성된 설명을 영어로 번역하는 체인 추가
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
#오픈AI의 대규모 언어 모델 설정
model = ChatOpenAI(model= "gpt-4o-mini")

#프롬프트 템플릿 정의 : 주어진 주제에 대한 설명 요청
prompt = ChatPromptTemplate.from_template("주제 {topic}에 대해 설명 해주세요.")

#출력 파서 정의 : AI 메시지의 출력 내용을 추출
parser = StrOutputParser()

#프롬프트, 모델, 출력 파서를 체인으로 연결
chain = prompt | model | parser


#"이 대답을 영어로 번역해 주세요" 라는 질문을 생성하는 프롬프트 템플릿 정의
analysis_prompt = ChatPromptTemplate.from_template("이 대답을 영어로 번역해 주세요 : {answer}")

#이전에 정의된 체인과 새로운 작업을 연결하는 체인 구성
composed_chain = {"answer": chain} | analysis_prompt | model | StrOutputParser()
#LG트윈스라는 주제로 응답을 생성하고 체인 실행
response = composed_chain.invoke({"topic" : "LG트윈스"})

print(response)