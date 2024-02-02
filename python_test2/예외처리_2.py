# try / except

try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없음")
except IndexError:
    print("인덱싱 할 수 없음")