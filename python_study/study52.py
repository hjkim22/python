# set = 집합, 합집합, 교집합, 차집합 등
# 대표적으로 합집합, 교집합, 차집합을 유용하게 사용함

채소1 = {"당근", "양파", "오이", "배추"}
채소2 = {"양파", "오이", "대파", "가지"}

# 합집함(union)
print(채소1 | 채소2)
print(set.union(채소1, 채소2))

# 교집합(intersection)
print(채소1 & 채소2)
print(set.intersection(채소1, 채소2))

# 차집합(difference
print(채소1 - 채소2)
print(set.difference(채소1, 채소2))