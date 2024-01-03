# # tuple 쓰는 이유
# # 더 돋보이게 만들 수 있음

# 1. 3GO가 불가하기 때문 (추가, 삭제, 변경)
#     여러명이 코딩을 하는 경우 변경되면 안되는 변수를 건드리는 경우
#     또는 값이 변경되면 안되는 중요한 데이터를 넣어서 보안적으로 관리하기 좋다
#     (은행계좌, 비밀번호 등..)

# 2. list는 tuple보다 무겁다.
#     단지 기능이 많아서 무거운건가?
#     파이썬은 c로 만들어졌다.

#     파이썬은 동적배열을 지원한다.
#     - list = [1, 2, 3, 4] 생성해서 4개에 값을 모두 넣음.
#     - 문제는 그 다음 값을 추가할때 이미 공간이 다 찼기 때문에 추가 할당을 진행한다.
#         추가 할당 시 메모리 크기는 4, 8, 16... 더블링을 해줌

# 3. 리스트는 가변, 튜플은 불변이다.
#     값이 고정 되어야 하거나 크기가 작을 경우 튜플을 권장한다.






    # 공부할 것

# 가변객체와 불변객체 (이미 다 써봄)
# 파이썬 리스트와 동적배열