#문자열 프롬프트 템플릿 생성하기

from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
prompt_template = PromptTemplate.from_template("주제{topic}에 대해 금융 관련 짧은 조언을 해주세요")
#'투자' 주제로 프롬프트 템플릿 호출
result = prompt_template.invoke({"topic" : "투자"})

print(result)