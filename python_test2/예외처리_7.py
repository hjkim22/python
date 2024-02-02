# 오류 일부러 발생시키기

class Bird:
    def fly(self):
        raise NotImplementedError
    
class Eagle(Bird):
    pass
    # def fly(self):
    #     print("펄럭펄럭")

eagle = Eagle()
eagle.fly()

# 강제로 Eagle안에 메소드오버라이딩을 통해 fly 를 한번더 정의를 하게 끔 강제함