# 표준 체중을 구하는 프로그램을 작성하시오
# 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) x 키(m) x 22
# 여자 : 키(m) x 키(m) x 21

# 조건1 : 표준 체중은 별도의 함수 내에서 계산
#     * 함수명 : std_weight
#     * 전달값 : 키(height), 성별(gender)

# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175Cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender):
    if gender == "남":
        weight = round(height**2 * 22, 2)
    elif gender == "여":
        weight = round(height**2 * 21, 2)
    else:
        print('"남"/"여"로 입력하라고')
    return weight

height = float(input("키를 입력하세요(cm) : "))
gender = input("성별을 입력하세요. (남/여) : ")

std_weight_result = std_weight(height / 100, gender)

print(f'키 {height}cm, {gender}자의 표준 체중은 {std_weight_result}kg 입니다.')