'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : 리스트의 객체 생성과 참조
'''
fruits1 = ['딸기', '수박', '바나나']

# 실제 값을 복사하는 것이 아니라 리스트의 저장
fruits2 = fruits1

print("fruits1 : ", fruits1)
print("fruits2 : ", fruits2)

fruits2[1] = '망고' # fruits2의 [1]번지 과일을 망고로 바꾼다.

print("fruits1 : ", fruits1)    # 모두 1번지 내용이 망고로 바뀐다.
print("fruits2 : ", fruits2)    # 주소를 참조하기 때문(같은 주소)

# 주소 확인 => 메모리 위치 정보 알아보기 id()함수
print("fruits1의 id : ", id(fruits1))
print("fruits1의 id : ", id(fruits2))