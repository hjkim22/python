# try / else

try:
    age = int(input('나이을 입력하세요 : '))
except:
    print('숫자만 입력해주세요')
else:
    if age <= 19:
        print('미성년자 출입그지')
    else:
        print('환영합니다.')