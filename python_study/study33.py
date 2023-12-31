# 슬라이싱

로또 = [3, 5, 15, 33, 41, 44]
# 로또 변수에 있는 리스트의 인덱스 1번부터 2번까지의 값을 출력
print(로또[1:3])

# 로또 변수의 마지막 위치 출력
print(로또[-1])

# 반대로 출력
print(로또[::-1])

# 로또 리스트안에 33이 있는지 확인
print(33 in 로또)

#로또 리스트를 로또2 리스트와 합치기
로또2 = [2, 12, 15, 24, 33, 39]
print(로또 + 로또2)

# range를 이용해서 1부터 10사이에 짝수만 들어있는 짝수 (변수명) 리스트 생성
짝수 = list(range(2,12,2))
print(짝수)

# 짝수 리스트에 들어있는 값을 2배늘리고 다시 짝수 변수에 담아 출력
짝수 = 짝수 * 2
print(짝수)

# 짝수 리스트에 들어있는 요소의 개수를 출력
print(len(짝수))

# 짝수 리스트에 3번째 인덱스를 출력
print(짝수[3])

# len()함수를 이용해 인덱스 마지막 값을 출력
print(짝수[len(짝수)-1])