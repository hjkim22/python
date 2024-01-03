# set
# set은 수학의 집합을 의미
# 딕셔너리와 같이 순서가 없음
# 값의 중복을 허락하지 않음 (아주 중요)
# 생성방법 : {}

채소 = {"당근", "배추", "대파", "양파"}

print(type(채소))
print(채소)

# 순서가 없고, 출력하면 요소가 다르게 나온는것도 특징

# set를 만드는 다양한 방법
채소2 = {}
채소3 = set()
print(채소3)

# 중복을 제일 싫어하는 set
사과_리스트 = list("apple")
print(사과_리스트)
사과_튜플 = tuple("apple")
print(사과_튜플)
사과_set = set("apple")
print(사과_set)