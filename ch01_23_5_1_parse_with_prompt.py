from langchain.output_parsers import RetryWithErrorOutputParser
from langchain_core.output_parsers import JsonOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# .env 파일에서 OPENAI_API_KEY 불러오기
load_dotenv()


#파서 설정
parser = RetryWithErrorOutputParser.from_llm(parser=JsonOutputParser(),  
                                             llm=ChatOpenAI())
#RetryWithErrorOutputParser는 오류 발생 시 재시도 기능을 제공
#JsonOutputParser는 내부 파서로 사용-> JSON 형식으로 파싱
#ChatOpenAI를 LLM모델로 활용하여 오류 수정 요청할 수 있음

question = "가장 큰 대륙은?"
ai_response = "아시아입니다" #JSON 형식이 아닌 잘못된 응답

try:
    result = parser.parse_with_prompt(ai_response,question)
    print(result)
except Exception as e:
    print(f"오류 발생: {e}")
    #여기서 AI에게 다시 질문 가능
    

