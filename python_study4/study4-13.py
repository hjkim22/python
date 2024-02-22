# 34.5 게임 캐릭터 클래스 만들기

class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
    def slash(self):
        print('베기')

x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

# 542.4 210.3 38
# 베기