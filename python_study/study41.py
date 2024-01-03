# 시퀀스 자료형 공통점
튜플 = (3, "아", 2.4)
print(튜플)

# 길이를 구할 수 있음
print(len(튜플))

# 곱하기 연산으로 요소를 복사할 수 있음
튜플 = 튜플 * 2
print(튜플)

# 요소들끼리 더할 수 있다.
튜플 = 튜플 + 튜플
print(튜플)

# 인덱싱이 가능
print(튜플[2])

# 튜플의 인덱스
print(튜플.index(2.4))

# 튜플 요소의 개수
print(튜플.count("아"))

# 슬라이싱이 가능
print(튜플[1:3])