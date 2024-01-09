# # 퀴즈 3

# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# ex) hthp://naver.com
# 규칙1 : http:// 부분은 제외 > naver.com
# 규칙2 : 처음 만나는 점. 이후 부분은 제외 > naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수 + "!" 로 구성
# ex) 생성된 비밀번호 : nav51!

# url = "http://naver.com"
# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print(f'{url} 사이트의 생성된 비밀번호 : {pw}')


# 리펙토링
new_link = input("사이트 주소를 입력하세요.")
my_str = new_link.replace("http://", "")
my_str = my_str[:my_str.index(".")]
pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print(f'{new_link} 사이트의 생성된 비밀번호 : {pw}')