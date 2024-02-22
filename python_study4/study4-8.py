# 33.2
# nonloca이 변수를 찾는 순서

def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x # 20
            nonlocal y # 100
            x = x + 30
            y = y + 300
            print(x) # 50
            print(y) # 400
        C()
    B()
A()

# global로 전역 변수 사용
# 함수가 몇 단계든 상관없이 global 키워드를 사용하면 무조건 전역 변수를 사용
x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            global x
            x = x + 30
            print(x)
        C()
    B()
A()
# global을 사용하면 전역 변수를 사용하게 됨
# 전역 변수는 코드가 복잡해졌을때 변수의 값을 어디서 바꾸는지 알기가 힘들어서 가급적 사용하지 않는게 좋음
        