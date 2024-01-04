class Person:
    def __init__(self, name, age, adderess):
        self.hello = "안녕"
        self.name = name
        self.age = age
        self.adderess = adderess

    def greeting(self):
        print('{0} 나는 {1}.'.format(self.hello, self.name))

maria = Person('마리아', 20, "서울")
maria.greeting()

print("이름:", maria.name)
print("나이:", maria.age)
print("주소:", maria.adderess)