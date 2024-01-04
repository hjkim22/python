# 예외코드 작성

try:
    x = int(input("나눌 숫자 입력"))
    y = 10 / x
    print(y)
except:
    print("예외 발생")