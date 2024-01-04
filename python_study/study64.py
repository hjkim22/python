# while 문에도 else가 있다.

양파 = 10
while 양파 > 10:
    print("양파", 양파, "개 남음")
    if 양파 == 0:
        break
        양파 -= 1
    else:
        print("다팔림")
