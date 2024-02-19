# 32.2
# 람다 표현식, map, filter, reduce 함수

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))



print(list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a)))
# ↓
def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10
print(list(map(f, a)))



# map에 객체 여러개 넣기
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x * y, a, b)))



# filter
def f(x):
    return 5 < x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]

print(list(filter(f, a)))
# ↓
print(list(filter(lambda x: 5 < x < 10, a)))




# reduce
from functools import reduce

def f(x, y):
    return x + y
a = [1, 2, 3, 4, 5]
print(reduce(f, a))
# ↓
print(reduce(lambda x, y: x + y, a))