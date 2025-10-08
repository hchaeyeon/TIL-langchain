#라이브러리 불러오기
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
#오픈AI의 대규모 언어 모델 설정
model = ChatOpenAI(model= "gpt-4o-mini")

#프롬프트 템플릿 정의 : 주어진 주제에 대한 설명 요청
prompt = ChatPromptTemplate.from_template("주제 {topic}에 대해 설명해주세요.")

#출력 파서 정의 : AI 메시지의 출력 내용을 추출
parser = StrOutputParser()

#프롬프트, 모델, 출력 파서를 체인으로 연결
chain = prompt | model | parser

for token in chain.stream({"topic" : "더블딥"}):
    
#스트리밍된 내용 출력, 각 내용을 붙여서 출력하며 버퍼를 즉시 플러시하여 실시간으로 보여줌
    print(token, end="", flush=True)
    ##생성된 텍스트를 한번에 출력하는 대신 생성된 토큰을 하나씩 출력!!
    ##flush=True는 출력 버퍼를 즉시 플러시하여, 결과를 지연 없이 실시간으로 화면에 보여줌