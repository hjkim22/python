# 반복문에 흐름을 제어하는 continue와 break

i = 0
while True:
    print(i)
    i += 1
    if i == 3:
        break

for i in range(5):
    print(i)
    if i == 5:
        break

i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

i = 0
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)