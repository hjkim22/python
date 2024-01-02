mzfood = ["숙주", "분모자", "마라", "소세시", "양고기", "옥수수면"]
print(mzfood)

# print(dir(list))
mzfood.reverse()
print(mzfood)

mzfood.sort()
print(mzfood)

# print(mzfood.reverse())
# 위 코드가 변형만 되고 출력이 안되는 이유
# 해당 메소드의 성격떄문이다.
# 리스트를 직접 변경하고, 새로운 리스트를 반환하지 않음