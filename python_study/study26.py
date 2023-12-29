# # 변수값 입력
# fish__p, fish__s, fish__j = "붕어빵(팥)", "붕어빵(슈크림)", "붕어빵(잡채"
# fish__p__sell, fish__s__sell, fish__j__sell = 2000, 2500, 3000
# order__s = 2
# order__j = 3

# # 붕어빵 계산값
# order__s__pay = fish__s__sell * 2
# order__j__pay = fish__j__sell * 3
# total__order = order__s + order__j
# total_pay = order__s__pay + order__j__pay
# print(f'주문이 완료되었습니다. {fish__s} {order__s}개, {fish__j} {order__j}개 총 {total__order}개 결제 금액은, {total_pay}원 입니다.')




# 레거시 : 누군가 남겨두고간 코드
# 리팩토링 : 결과의 변경 없이 코드의 구조를 재조정하는 것

# 변수값 입력

fish__p, fish__s, fish__j = input('붕어빵(팥), "붕어빵(슈크림), 붕어빵(잡채)를 순서대로 쉼표를 포함하여 입력하세요. 선택하지 않을 경우 0을 넣어주세요.').split(",")

fish__p__sell, fish__s__sell, fish__j__sell = 2000, 2500, 3000

order__p, order__s, order__j = map(int,input('쉼표를 사용하여 각 붕어빵 개수를 입력하세요. 선택하지 않을 경우 0을 넣어주세요.').split(","))


# 붕어빵 계산값
order__p__pay = fish__p__sell * order__p
order__s__pay = fish__s__sell * order__s
order__j__pay = fish__j__sell * order__j

total__order = order__p + order__s + order__j
total_pay = order__p__pay + order__s__pay + order__j__pay

print(f'주문이 완료되었습니다. {fish__p} {order__p}개, {fish__s} {order__s}개. {fish__j} {order__j}개 총 {total__order}개 결제 금액은, {total_pay}원 입니다.')

