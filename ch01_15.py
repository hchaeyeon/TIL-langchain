#메시지 자리 표시자 활용하여 프롬프트 템플릿 구성_MessagePlaceholder클래스를 사용하여 챗 프롬프트 템플릿 정의

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

#(방법1) 메시지 자리 표시자를 포함한 챗 프롬프트 템플릿 정의
prompt_template = ChatPromptTemplate.from_messages([
    ("system", "당신은 유능한 금융 조언가입니다."),
    MessagesPlaceholder("msgs")
])

#메시지 리스트를 'msgs' 자리 표시자에 전달하여 호출
result = prompt_template.invoke({"msgs" : [HumanMessage(content="안녕하세요!")]})
print(result)
