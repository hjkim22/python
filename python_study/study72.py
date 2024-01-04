class Person:
    def __init__(self):
        self.hello = "안녕하세요"

    def greeting(self):
        print(self.hello)

호출 = Person()
호출.greeting()