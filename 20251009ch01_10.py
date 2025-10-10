#파이스 연산자 예제를 .pipe() 메서드로 구성한 예제
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model= "gpt-4o-mini")
prompt = ChatPromptTemplate.from_template("{topic}에 대해 설명 해주세요.")
chain = prompt | model | StrOutputParser()
analysis_prompt = ChatPromptTemplate.from_template("이 대답을 영어로 번역해 주세요 : {answer}")

#(방법1) 여러 작업을 순차적으로 .pipe를 통해 연결하여 체인 구성하기
composed_chain_with_pipe = (
    chain
    #입력된 데이터를 "answer" 키로 변환하는 람다 함수 적용
    .pipe(lambda input: {"answer" : input})
    #analysis_prompt를 체인에 연결하여 설명을 영어로 번역하는 작업 추가
    .pipe(analysis_prompt)
    #모델을 사용해 응답
    .pipe(model)
    #생성된 응답을 문자열로 파싱
    .pipe(StrOutputParser())
)

response = composed_chain_with_pipe.invoke({"topic" : "KBO"})
print(response)