# 아래 ice 딕셔너리에 데이터를 추가 후 출력해주세요

# ice = {"메로나": [300, 20],
# "비비빅": [400, 3],
# "죠스바": [250, 100]}

# 추가해야하는 데이터 : 이름 : 보석바, 가격:650, 재고:10

ice = {"메로나": [300, 20],
       "비비빅": [400, 3],
       "죠스바": [250, 100]}

ice.update({"보석바": [650, 10]})

print(ice)