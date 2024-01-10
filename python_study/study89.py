# 기본값

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 언어 : {2}"\
#         .format(name, age, main_lang))
    
# profile("KIM", 20, "python")
# profile("LEE", 21, "java")

def profile(name, age=17, main_lang="python"):
    print("이름 : {0}\t나이 : {1}\t주 언어 : {2}"\
        .format(name, age, main_lang))
    
profile("KIM")
profile("LEE")