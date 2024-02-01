def add(a, b):
    return a + b

def sub(a, b): 
    return a-b
# print(add(3, 4))


# 외부에서 사용 시.

# 다른 파일에서 import module_1 을 실행하면 
# print(add(3, 4)) 값까지 출력됨

# 해당 파일인 내부에서만 print를 사용하기 위해 아래 코드를 사용

if __name__ == "__main__":
    print(add(3, 4))