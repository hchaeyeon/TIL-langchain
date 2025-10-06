#아래의 라이브러리들은 랭체인을 구성하고 API와 상호작용하는 데 중요한 역할을 함.

from langchain_openai import ChatOpenAI #ChatOpenAI는 랭체인에서 오픈AI의 GPT 모델을 사용하는 클래스
from langchain_core.prompts import ChatPromptTemplate #ChatPromptTemplate은 프롬프트 템플릿을 만들어주는 클래스
from langchain_core.output_parsers import StrOutputParser #StrOutputParser는 GPT 모델이 반환한 응답을 문자열로 변환하는 역할
from langchain_core.runnables import RunnablePassthrough #RunnablePassthrough는 입력 데이터를 그대로 통과시키는 역할
from dotenv import load_dotenv #.env 파일에서 환경 변수를 불러오는데 사용

load_dotenv() 
#주어진 주제에 대해 짧은 설명을 요청하는 프롬프트 템플릿 정의
prompt = ChatPromptTemplate.from_template(
    "주제 {topic}에 대해 짧은 설명을 해주세요."
)
#출력 파서를 문자열로 설정
output_parser = StrOutputParser()

#오픈 AI의 gpt-4o 모델을 사용하여 채팅 모델 설정
model = ChatOpenAI(model="gpt-4o")

chain = (
    {"topic" : RunnablePassthrough()} #입력받은 주제를 그대로 통과시킴
    |prompt                           #프롬프트 템플릿 적용
    |model                            #모델을 사용해 응답 생성
    |output_parser                    #응답을 문자열로 파싱
)

#"KBO" 주제로 설명 요청
result = chain.invoke("KBO")
print(result)