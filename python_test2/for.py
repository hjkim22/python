# 주어진 정수 x와 자연수 n을 이용해, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 출력해주세요

# x = 2, n =5

x = 2
n = 5

result = list()

for i in range(n):
    result.append(x * i + x)

print(result)