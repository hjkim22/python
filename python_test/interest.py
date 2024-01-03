# 성과급으로 2500만원을 받았습니다.
# 연이율 6.15%의 고정금리 상품에 예금하려고 합니다.
# 3년 동안 넣어두면 원금을 제외한 이자가 얼마나 되는지 계산해 주세요

# (이자 지급 방식은 매년 원금 기준으로 지급되는 단리 방식입니다.)
# 원금 25000000원, 연이율 6.15%, 기간 : 3년
 
principal = 25000000
air = 6.15  # annual interest rate
period = 3

interest = principal * (air / 100)

revenue = interest * period

revenue_formatted = '{:,.0f}'.format(revenue)

print(f'원금을 제외한 3년간 이자는 {revenue_formatted}원 입니다.')