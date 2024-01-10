from random import *

count = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print(f'[0] {i}번째 손님 (소요시간 : {time}분)')
        count += 1
    else:
        print(f'[ ] {i}번째 손님 (소요시간 : {time}분)')
print(f'총 탑승 승객 : {count}명')