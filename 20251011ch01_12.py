#RunnableParallel클래스를 통해 동일한 주제에 대해 한국어와 영어로 설명을 생성하는 두개의 체인을 병렬로 실행

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()
#OpenAI 모델 초기화
model = ChatOpenAI()

#한국어 설명 생성 프롬프트 체인
kor_chain = (
    ChatPromptTemplate.from_template("{topic}에 대해 짧은 설명 해주세요.")
    |model
    |StrOutputParser()
)

#영어 설명 생성 프롬프트 체인
eng_chain = (
    ChatPromptTemplate.from_template("{topic}에 대해 짧게 영어로 설명을 해주세요.")
    |model
    |StrOutputParser()
)

#병렬 실행을 위한 RunnableParallel 설정
parallel_chain = RunnableParallel(kor=kor_chain, eng=eng_chain)

#주제에 대한 한국어와 영어 설명 생성
result = parallel_chain.invoke({"topic" : "LG트윈스"})

print("한글 설명:", result['kor'])
print("영어 설명:", result['eng'])