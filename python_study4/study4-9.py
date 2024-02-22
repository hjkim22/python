# 33.3
# 클로저 사용

def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 변환

c = calc()
print(c(1), c(2), c(3), c(4), c(5))
# 함수 calc가 끝났는데도 c는 calc의 지역 변수 a, b를 사용해서 계산하고 있음
# 이렇게 함수를 둘러싼 환경을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수를 클로저라고함
# 여기서는 c에 저장된 함수가 클로저


# lambda로 클로저 만들기
def calc():
    a = 3
    b = 5
    return lambda x: a * x + b

c = calc()
print(c(1), c(2), c(3), c(4), c(5))

# 클로저 지역 변수 변경
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
c = calc()
c(1)
c(2)
c(3)