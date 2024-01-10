# pickle

# import pickle
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"KIM", "나이":30, "취미":["헬스","음주"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()


import pickle
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()