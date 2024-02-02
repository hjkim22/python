# 표준라이브러리
# 내장된게 아니고 임포트해서 쓰는것
# 임포트해서 쓰되 따로 설치하지 않고 인포트라는 명령어와 함께 사용

# _____________________________________________

# import datetime : 연, 월, 일로 날짜를 표현할 때 사용하는 함수

# import datetime
# day1 = datetime.date(2023, 12, 7)
# day2 = datetime.date(2024, 2, 2)

# diff = day2 - day1
# print(diff.days)

# _____________________________________________

# time.time : UTC(universal time coordinated, 협정 세계 표준시)를 사용하여 현재 시간을 실수 형태로 리턴하는 함수
# 1970년 1월 1일 0시 0분 0초를 기준으로 지난 시간을 초 단위로 리턴
# import time
# print(time.time())

# _____________________________________________

# time.sleep : 주로 루프 안에서 많이 사용한다. 이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다.
# import time
# for i in range(10):
#     print(i)
#     time.sleep(1)

# _____________________________________________

# random : 난수(규칙이 없는 임의의 수)를 발생시키는 모듈

import random
# print(random.random())
# print(random.randint(1, 10))
# print(random.randint(1, 55))


def random_pop(data):
    number = random.randint(0, len(data)-1)
    return data.pop(number)

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data: 
        print(random_pop(data))
# 위에서 만든 random_pop 함수는 리스트의 요소 중에서 무작위로 하나를 선택하여 꺼낸 다음 그 값을 리턴한다. 꺼낸 요소는 pop 메서드에 의해 사라진다.
