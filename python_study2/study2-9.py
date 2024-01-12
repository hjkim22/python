# class
# 다중상속

# 일반 유닛
class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군 공격 [공격력 {}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력 {}".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


# 드랍쉽 : 공중 유닛, 수송기, 마린/파이어뱃/탱크 등을 수송, 공격 불가

# 날 수 있는 기능을 가진 클래스
class Flyalbe:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyalbeAttackUnit(AttackUnit, Flyalbe):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyalbe.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛, 한번에 14방 미사일 발사.
valkyrie = FlyalbeAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

