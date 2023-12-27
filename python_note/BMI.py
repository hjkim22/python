# 신체질량지수(BMI) = 체중(kg) / [신장(m)]²

# 저체중   20미만
# 정상    20~24
# 과제충   25~29
# 비만    30이상

height = 183
weight = 78

height_m = height / 100

bmi = (weight / (height_m ** 2))

if bmi < 20:
    result = "저체중"
elif 20 <= bmi < 25:
    result = "정상"
elif 25 <= bmi < 30:
    result = "과체중"
else:
    result = "비만"

bmi = round(bmi, 1) # 소수점 반올림

print(f'당신의 BMI는 {bmi}이고 비만도는 {result}입니다.')