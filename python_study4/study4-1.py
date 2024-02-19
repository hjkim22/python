# 32.1
# 람다 표현식 함수

def plus_ten(x):
    return x + 10
print(plus_ten(1))
# ↓
plus_ten = lambda x: x + 10
print(plus_ten(1))



print((lambda x: x + 10)(1))


y = 10
print(((lambda x: x + y))(1))


def plus_ten(x):
    return x + 10
print(list(map(plus_ten, [1, 2, 3])))


print(list(map(lambda x: x + 10, [1, 2, 3])))



# 람다 표현식으로 매개변수가 없는 함수 만들기
print((lambda : 1)())

x = 10
print((lambda : x)())