# 예외처리
# ㄴ 오류가 발생했을때 어떻게 할지 정하는 것

# try / except

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

# 오류를 잡았기 때문에 프린트 실행
# 오류가 발생하면 오류를 잡아서 처리하는 개념