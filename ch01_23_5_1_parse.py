from langchain_core.output_parsers import JsonOutputParser

#Json 출력 파서 불러오기
parser = JsonOutputParser()

ai_response = '{"이름":"김철수", "나이":30}'
parsed_response = parser.parse(ai_response)

print(parsed_response)