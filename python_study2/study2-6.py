# class
# 멤버변수

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛 생성.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))

# marine1 = Unit("마린", "40", "5")
# marine2 = Unit("마린", "40", "5")
# tank = Unit("탱크", "150", "35")

# 레이스 : 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage))

# 마인드 컨틀로 : 상대방 유닛을 내 것으로 만드는 것 (빼았음)
wraith2 = Unit("빼았은 레이스", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))