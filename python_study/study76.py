class Car(object):
    maxspeed = 300
    maxpeople = 5
    def move(self, x):
        print("스피드로 달리고 있습니다.")
    def stop(self):
        print("멈췄습니다.")
class HybridCar (Car ):
    battery = 1000
    batteryKM = 300
class ElectricCar ( HybridCar):
    battery = 1000
    batteryKM = 300
    def move(self, x):
        print(self.batteryKM, "만큼 달릴 수 있습니다.")
        print(x, '스피드로 달리고 있습니다. ')
k5 = HybridCar ()
k5.maxspeed

electricCark5 = ElectricCar ()
electricCark5.maxspeed
electricCark5.battery 
electricCark5.move(10)

# print (dir (k5))