# 클래스의 상속

# 기반 클래스 > 기능을 물려'주는' 클래스
# 파생 클래스 > 기능을 물려'받는' 클래스

class Car (object):
    maxspeed = 300
    maxpeople = 5

    def move(self, x):
        print("스피드로 달리고 있습니다.")
    def stop(self):
        print("멈췄습니다.")

class HybridCar (Car):
    battery = 1000
    batteryKM = 300

k5 = HybridCar ()
print(k5.maxspeed)

# print (dir (k5))