# 붕어빵 철이 돌아왔죠
# 붕어빵(팥) : 2000원, 붕어빵(슈크림) : 2500원, 붕어빵(잡채) : 3000원
# 무인 주문기계를 만들어주세요.

# 붕어빵(잡채) 3개, 붕어빵(슈크림) 2개를 주문하면
# "주문이 완료되었습니다. 붕어빵(슈크림) 2개, 붕어빵(잡채) 3개 총 5개 결제 금액은, 14000원 입니다."
# 이 출력되도록 코드를 작성해주세요.
# 변수를 만들때 스네이크 케이스에 언더바는 2개 / print()문의 포메팅 f-string

# 변수값 입력
fish__p, fish__s, fish__j = "붕어빵(팥)", "붕어빵(슈크림)", "붕어빵(잡채"
fish__p__sell, fish__s__sell, fish__j__sell = 2000, 2500, 3000
order__s = 2
order__j = 3


# 붕어빵 계산값
order__s__pay = fish__s__sell * 2
order__j__pay = fish__j__sell * 3
total__order = order__s + order__j
total_pay = order__s__pay + order__j__pay

print(f'주문이 완료되었습니다. {fish__s} {order__s}개, {fish__j} {order__j}개 총 {total__order}개 결제 금액은, {total_pay}원 입니다.')

