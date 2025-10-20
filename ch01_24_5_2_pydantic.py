from langchain_core.output_parsers import PydanticOutputParser
#PydanticOutputParser는 랭체인에서 제공하는 도구, 대규모 언어 모델이 생성한 텍스트를 구조화된 데이터로 변환하는데 사용
    #Pydantic과 함께 사용하여 AI가 생성한 자유 형식의 텍스트를 개발자가 설정한 데이터 구조에 맞춰 자동으로 변환하며, 그 과정에서 데이터 유효성을 확인.

from langchain_core.prompts import PromptTemplate
#프롬프트 동적으로 생성하여 AI에게 전달할 질문과 출력 형식 지침을 설정
    #변수를 포함하여 다양한 입력 처리 가능
    
from langchain_openai import ChatOpenAI
#오픈AI의 GPT-4o 모델을 랭체인을 통해 사용할 수 있도록 지원, AI모델에 질문을 던지고 응답 받는 역할

from pydantic import BaseModel, Field, model_validator
#Pydantic : Python에서 데이터 검증과 모델링을 위한 라이브러리.
    #BaseModel과 Field를 사용하여 데이터 구조를 정의하고, model_validator를 통해 입력 데이터 검증 가능
from dotenv import load_dotenv


load_dotenv()
#OpenAI모델 설정
model = ChatOpenAI(model_name="gpt-4o", temperature=0.0) 

#원하는 데이터 구조 정의
class FinancialAdvice(BaseModel):
    setup: str = Field(description="금융 조언 상황을 설정하기 위한 질문")
    advice: str = Field(description="질문을 해결하기 위한 금융 답변")
    
    #Pydantic을 사용한 사용자 정의 검증 로직
    @model_validator(mode="before")
    @classmethod
    def question_ends_with_question_mark(cls, values: dict) -> dict:
        setup = values.get("setup", "")
        if not setup.endswith("?"):
            raise ValueError("잘못된 질문 형식입니다! 질문은 '?'로 끝나야 합니다")
        return values   
    
#차서 설정 및 프롬프트 템플릿에 지침 삽입
parser = PydanticOutputParser(pydantic_object=FinancialAdvice)
prompt = PromptTemplate(
    template = "다음 금융 관련 질문에 답변해 주세요. \n{format_instructions}\n질문:{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
#언어 모델을 사용해 데이터 구조를 채우도록 프롬프트와 모델 설정
chain = prompt | model | parser

#체인 실행 및 결과 출력
try :
    result = chain.invoke({"query": "부동산에 관련하여 금융 조언을 받을 수 있게 질문하라."})
    print(result)
except Exception as e:
    print(f"오류 발생:{e}")

#try-except 구문 = 오류 발생을 대비해 프로그램의 안정성 유지 + 발생한 오류를 쉽게 디버깅할 수 있도록 처리
