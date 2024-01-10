# print("Python", "Java", "JS", sep=",", end="? ")
# print("뭐할래?")


# import sys
# print("Python", "Java", "JS", file=sys.stdout)
# print("Python", "Java", "JS", file=sys.stderr)


# 시험 성적
# scores = {"수학":0, "영어":10, "코딩":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")


# 은행 대기순번표
# 001, 002, 003, ...
# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3))


answer = input("아무 갑이나 입력하세요 : ")
# input 타입 확인!
print("입력한 값은 " + answer + " 입니다.")