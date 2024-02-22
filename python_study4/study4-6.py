# 33.2 함수 안에서 함수 만들기
# 지역 변수 범위

def print_hello():
    hello = 'Hello World'
    def print_message():
        print(hello)
    print_message()

print_hello()
# 바깥쪽 함수의 지역 변수는 그 안에 속한 모든 함수에서 접근할 수 있음