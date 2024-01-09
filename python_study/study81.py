# 문자열포맷

# 1
print("방법 %d번" %1)
print("방법 %s" % "첫번째")
print("포맷은 %c로 시작" % "F")
print("%s색과 %s색" % ("파란", "빨간"))

# 2
print("나는 {}살입니다.".format(28))
print("나는 {}색과 {}색을 좋아한다.".format("파란","빨간"))
print("나는 {1}색과 {0}색을 좋아한다.".format("파란","빨간"))

# 3
print("나는 {age}살이고, {color}색을 좋아한다.".format(age = 20, color = "빨간"))

# 4
age, color = 20, "빨간"
print(f'나는 {age}살이고, {color}색을 좋아한다.')