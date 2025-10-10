#파이프 연산자 예제를 .pipe() 메서드로 구성한 예제
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model= "gpt-4o-mini")
prompt = ChatPromptTemplate.from_template("{topic}에 대해 설명 해주세요.")
chain = prompt | model | StrOutputParser()
analysis_prompt = ChatPromptTemplate.from_template("이 대답을 영어로 번역해 주세요 : {answer}")

#(방법2) 좀 더 간단하게 연결하기
composed_chain_with_pipe = chain.pipe(lambda input: {"answer" : input}, analysis_prompt, model, StrOutputParser())

response = composed_chain_with_pipe.invoke({"topic" : "KBO"})
print(response)