# # 지역변수 / 전역변수

# gun = 10

# def checkpoint(soldiers):
#     gun = 20
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {}".format(gun))

# print("전체 총 : {}".format(gun))
# checkpoint(2)
# print("남은 총 : {}".format(gun))

#--------------------------------------------#

gun = 10

def checkpoint(soldiers):
    global gun
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {}".format(gun))

print("전체 총 : {}".format(gun))
checkpoint(2)
print("남은 총 : {}".format(gun))