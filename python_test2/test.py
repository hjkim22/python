# 전화번호가 문자열 phone_number로 주어졌을 때, 
# 전화번호의 뒷 4자리를 *으로 가린 문자열이 출력되도록 코드를 작성해주세요

# phone_number = "01012347890"

# 출력 예시 : "0101234****"

phone_number = "01012347890"

hidden_number = phone_number[:-4] + "****"

print(hidden_number)