#메시지 자리 표시자 활용하여 프롬프트 템플릿 구성_placeholder라는 문자열과 {msgs}란는 변수를 사용하여 자리 표시자 구현

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

#(방법2) MessagesPlaceholder 클래스를 사용하지 않고 비슷한 작업 수행
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "당신은 유능한 금융 조언가입니다"),
    ("placeholder", "{msgs}") # <- 여기서 'msgs'가 자리 표시자로 사용됩니다.
])

#메시지 리스트를 'msgs' 자리 표시자에 전달하여 호출
result = prompt_template.invoke({"msgs" : [HumanMessage(content="안녕하세요!")]})

print(result)