# pip install langchain langchain-openai langchain-chroma chromadb

import os
from langchain_chroma import Chroma
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_openai import OpenAIEmbeddings

# 1) OpenAI API 키 설정(둘 중 하나)
# 방법 A: 코드에서 직접
# os.environ["OPENAI_API_KEY"] = "sk-..."  # <- 여기에 본인 키
# 방법 B: 터미널에서 미리 export/set 해두기 (권장)

# 2) 임베딩 인스턴스
emb = OpenAIEmbeddings(model="text-embedding-3-small")  # 환경변수 OPENAI_API_KEY 사용

examples = [
    {
        "question": "주식 투자와 예금 중 어느 것이 더 수익률이 높은가?",
        "answer": """
후속 질문이 필요한가요: 네.
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

# 3) 예제 선택기 만들기
example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples=examples,
    embedding=emb,                # 임베딩 인스턴스
    vectorstore_cls=Chroma,       # 벡터스토어 클래스
    k=1,
    input_keys=["question"],      # <-- 핵심: 어떤 키를 임베딩할지 명시
)

# 4) 질의 및 선택
question = "부동산 투자의 장점은 무엇인가?"
selected_examples = example_selector.select_examples({"question": question})

print(f"입력 질문: {question}")
for ex in selected_examples:
    print("\n# 입력과 가장 유사한 예제")
    print(f"question: {ex['question']}")
    print(f"answer:\n{ex['answer']}")
