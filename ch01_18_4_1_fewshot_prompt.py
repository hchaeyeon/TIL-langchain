from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import PromptTemplate

example_prompt = PromptTemplate.from_template("질문: {question}\n 답변: {answer}")

# 퓨샷 예제 목록 생성
examples = [
    {
        "question": "주식 투자와 예금 중 어느 것이 더 수익률이 높은가?",
        "answer": """
후속 질문이 필요한가요: 네.e
후속 질문: 주식 투자의 평균 수익률은 얼마인가요?
중간 답변: 주식 투자의 평균 수익률은 연 7%입니다.
후속 질문: 예금의 평균 이자율은 얼마인가요?
중간 답변: 예금의 평균 이자율은 연 1%입니다.
따라서 최종 답변은: 주식 투자
""",
    },
    {
        "question": "부동산과 채권 중 어느 것이 더 안정적인 투자처인가?",
        "answer": """
후속 질문이 필요한가요: 네.
후속 질문: 부동산 투자의 위험도는 어느 정도인가요?
중간 답변: 부동산 투자의 위험도는 중간 수준입니다.
후속 질문: 채권의 위험도는 어느 정도인가요?
중간 답변: 채권의 위험도는 낮은 편입니다.
따라서 최종 답변은: 채권
""",
    },
]
#FewShotPromptTemplate 생성
prompt = FewShotPromptTemplate (
    examples = examples,
    example_prompt = example_prompt,
    suffix = "질문: {input}",
    input_variables=["input"],
    )

#'부동산 투자' 주제로 프롬프트 호출 및 출력
print(
    prompt.invoke({"input" : "부동산 투자의 장점은 무엇인가?"}).to_string()
)