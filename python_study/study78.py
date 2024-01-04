y = [10, 20, 30]
try:
    index, x = map(int, input("나눌 숫자 입력").split(","))
    print(y[index] / x)
except ZeroDivisionError:
    print('0으로 나눌 수 없음')
except IndexError:
    print('인덱스 에러.')
except:
    print('숫자만 입력.')