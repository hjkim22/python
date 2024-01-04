try:
    x = int(input("나눌 숫자 입력"))
    y = 10 / x
    #raise > 강제 에러 발생
    print(y)
except:
    print("예외 발생")
else:
    print("코드 실행 성공")
finally:
    print("코드 실행 종료")