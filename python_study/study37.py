# 시퀀스 자료형
# 문자열 :
#     시퀀스형에서 사용할 수 있는 메소드(count(), index(), split()등..)
#     슬라이싱([:], [::])
#     요소들로 이루어져 가능했던 기능(요소합치기, 요소 찾기 등)
# list :
#     시퀀스형에서 사용할 수 있는 메소드(count(), index(), split()등..)
#     슬라이싱([:], [::])
#     요소들로 이루어져 가능했던 기능(요소합치기, 요소 찾기 등)
#     list 지원하는 다양한 메소드(append(), insert(), sort(), reverse())
# tuple
    # 리스트처럼 요소를 일렬로 지정하지만 안에 저장된 요소를 변경,추가,삭제할 수 없음
    # 값을 추가, 삭제, 변경할 수 없기 때문에 사용하지 못하는 메소드가 많다.
    # tuple의 생성 방법은 tuple = 값, 값 또는 tuple = (값, 값)
    # 튜플은 소괄호.

# 리스트는 대괄호 [], 튜플은 소괄호()

튜플 = (1, "아", 3.0)
print(type(튜플))
print(튜플)

# 리스트 = [1, "아", 3.0]
# print(type(리스트))
# print(리스트)

튜플2 = 1, "아", 3.0
print(type(튜플2))
print(튜플2)

# 하나의 값만 들어있는 튜플만 만들고 싶다면?
튜플_솔로 = (1,)
print(type(튜플_솔로))
print(튜플_솔로)

튜플_솔로2 = (1)
print(type(튜플_솔로2))
print(튜플_솔로2)