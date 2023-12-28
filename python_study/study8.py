# 변수 : 하나의 값을 저장할 수 있는 공간을 생서하는 것
# 변수명을 만들때 컨벤션
# 변수를 표현하는 방법 : 스네이크, 카멜
# 변수를 활용해서 다양한 문제

# 1. int(integer) : 정수
# 2. float(float) : 실수
# 3. str(string) : 문자
# 4. bool(bool, boolean) : 참 또는 거짓, true 또는 false, 1 또는 0
# 5. list
# 6. tuple
# 7. dict
# 8. set

print(1.1 + 2)
print(4 / 2)

# 정수 : 1, 2, 3, -1, -2. -3
# 실수 : 1.2, 3.3, 4.0

print(9 + 2)
print(9.0 + 2)


# box_num에 숫자만 넣자는 약속을 했는데 누군가 한글 표기법으로 숫자를 넣음.

box_num = "하나"
box_num += 1
print(box_num) # 에러발생