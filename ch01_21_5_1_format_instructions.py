from langchain_core.output_parsers import JsonOutputParser

#Json 출력 파서 불러오기
parser = JsonOutputParser()
instructions = parser.get_format_instructions()
print(instructions) #Json 형식의 지침 출력