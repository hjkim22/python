# 예외 만들기

class MyError(Exception):
    pass
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick("바보")

# MyError 발생

# 셀프로 예외처리가 가능