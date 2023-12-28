# 2여야 하는데 형변환
# 4 / 2 > 2.0

# 말그대로 형태를 변형한다 : 형변환

# int, float, int > float 예) 5 > 5.0 float(5)

### print(float(5))
### print(int(5.0))


나이 = 10
type(나이)
### print(dir(나이))
# int 타입 안에 들어있는 기본적으로 들어있는 메소드와 기능

print(나이.bit_length()) # 0과 1
print(bin(나이)) # 10을 bit로 변환하면 4자리가 나옴
