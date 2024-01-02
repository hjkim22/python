# tuple 번회

수강생 = "중꺾그마"

수강생_list = list(수강생)
수강생_tuple = tuple(수강생)

print(수강생_list)
print(수강생_tuple)

수강생_list[1] = "뿌"
print(수강생_list)

# join 함수 공부 알고 있으면 코테에 도움됨
취뽀_수강생 = "" .join(수강생_list)
print(취뽀_수강생)