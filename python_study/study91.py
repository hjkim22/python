# 가변 인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {}\t나이 : {}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()
    

profile("KIM", 20, "python", "java", "c", "c++", "js", "c#")
profile("LEE", 21, "kotlin", "swift")