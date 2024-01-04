# dict 이력서를 작성,
# 붕어빵 인터네셔널 채용공고 조건
# 레거시 코드 리펙토링

# 붕어빵 철이 돌아왔죠
# 붕어빵(팥) : 2000원, 붕어빵(슈크림) : 2500원, 붕어빵(잡채) : 3000원
# 무인 주문기계를 만들어주세요.

# 붕어빵(잡채) 3개, 붕어빵(슈크림) 2개를 주문하면
# "주문이 완료되었습니다. 붕어빵(슈크림) 2개, 붕어빵(잡채) 3개 총 5개 결제 금액은, 14000원 입니다."
# 이 출력되도록 코드를 작성해주세요.
# 변수를 만들때 스네이크 케이스에 언더바는 2개 / print()문의 포메팅 f-string


# fish__p, fish__s, fish__j = input('붕어빵(팥), "붕어빵(슈크림), 붕어빵(잡채)를 순서대로 쉼표를 포함하여 입력하세요. 선택하지 않을 경우 0을 넣어주세요.').split(",")

# fish__p__sell, fish__s__sell, fish__j__sell = 2000, 2500, 3000

# order__p, order__s, order__j = map(int,input('쉼표를 사용하여 각 붕어빵 개수를 입력하세요. 선택하지 않을 경우 0을 넣어주세요.').split(","))


# # 붕어빵 계산값
# order__p__pay = fish__p__sell * order__p
# order__s__pay = fish__s__sell * order__s
# order__j__pay = fish__j__sell * order__j

# total__order = order__p + order__s + order__j
# total_pay = order__p__pay + order__s__pay + order__j__pay

# print(f'주문이 완료되었습니다. {fish__p} {order__p}개, {fish__s} {order__s}개. {fish__j} {order__j}개 총 {total__order}개 결제 금액은, {total_pay}원 입니다.')

주문_개수 = map(int, input(f'붕어빵 맛 순서대로 개수를 입력해주세요. 안살거면 0을 입력 / (팥, 슈크림 , 잡채)').split(","))

품목별_가격 = {"팥":2000, "슈크림":2500, "잡채":3000}

주문_개수 = list(주문_개수)
총_주문_개수 = sum(주문_개수)
total = 0

total += 품목별_가격["팥"] * 주문_개수[0]
total += 품목별_가격["슈크림"] * 주문_개수[1]
total += 품목별_가격["잡채"] * 주문_개수[2]

print(f'주문이 완료되었습니다. 팥 {주문_개수[0]}개, 슈크림 {주문_개수[1]}개, 잡채{주문_개수[2]}개 > 총{총_주문_개수}개, {total}원 입니다.')