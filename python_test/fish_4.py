# for문을 이용해 리펙토링 / input()....

fish = ["팥", "슈크림", "잡채"]
fish_price = [2000, 2500, 3000]

b_p = 0
b_s = 0
b_j = 0

order = input("붕어빵 종류와 개수를 입력해주세요. (예: 팥 1, 슈크림 2, 잡채 1): ")

order_list = order.split(", ")

for item in order_list:
    fish_type, quantity = item.split()
    quantity = int(quantity)

    if fish_type == "팥":
        b_p += quantity
    elif fish_type == "슈크림":
        b_s += quantity
    elif fish_type == "잡채":
        b_j += quantity

total_price = b_p * fish_price[0] + b_s * fish_price[1] + b_j * fish_price[2]

print(f'주문이 완료됐습니다. 팥 {b_p}개, 슈크림 {b_s}개, 잡채 {b_j}개 > 총 {b_p + b_s + b_j}개 주문하였습니다.')
print(f"총 가격은 {total_price}원 입니다.")