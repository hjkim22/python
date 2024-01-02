# list 값 넣고, 바꾸고, 지우고

mzfood = ["숙주", "분모자", "마라", "소세시", "소고기", "옥수수면"]

# 값을 넣는 방법 2가지
# append() : 마지막 요소에 값을 넣음
# insert() : 원하는 곳에 값을 넣음

mzfood.append("고수")
print(mzfood)

mzfood.insert(0, "탕후루")
print(mzfood)

# 값 지우기
del mzfood[-1]
print(mzfood)

del mzfood[0]
print(mzfood)

# 값 바꾸기
mzfood[-2] = "양고기"
print(mzfood)

# 문자열 시퀀스 아니냐 그럼 저거 다 되는거냐?
인사 = "반가워"
인사[2] = "웡"