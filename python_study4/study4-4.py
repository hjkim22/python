# 33.1
# 클로저
# 변수의 사용 범위

# x = 10          # 전역 변수
# def foo():
#     print(x)    # 전역 변수 출력

# foo()
# print(x)        # 전역 변수 출력

# def foo():
#     x = 10
#     print(x)

# foo()
# print(x)

x = 10
def foo():
    x = 20
    print(x)

foo()
print(x)