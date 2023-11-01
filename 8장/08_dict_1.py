'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : 8-1. 키와 같은 값을 가지고 딕셔너리
    
    튜플 = () 리스트 = [] 딕셔너리 = {}
'''
# 빈 딕셔너리 생성
phone_book1 = {}

# 딕셔너리에 값 저장. 1. key, valuse    [key] = value
phone_book1['임영훈'] = '010-9481-6853'

print('phone_book1 : ', phone_book1)    # {'임영훈' : '010-9481-6853'}

# 딕셔너리에 값 저장. 2. {key : value}
phone_book2 = {'홍길동' : '010-7638-6853', '임영훈' : '010-9481-6853'}
print('phone_book2 : ', phone_book2)

phone_book3 = {}
phone_book3['임영훈'] = '010-9481-6853'
phone_book3['홍길동'] = '010-7638-6853'
phone_book3['김개똥'] = '010-5827-6853'
phone_book3['김말똥'] = '010-2744-6853'
phone_book3['김소똥'] = '010-9010-6853'

print('phone_book3 : ', phone_book3)

print()
print(":: 전화번호 phone_book3 출력 ::")
# 모든 key 출력
print(phone_book3.keys())
# 모든 value 출력
print(phone_book3.values())
# 모든 key, value 출력
print(phone_book3.items())

print()
print(":: 전화번호 phone)book3 items()출력 :: ")
for name, phone_num in phone_book3.items() :
    print(name,':', phone_num)
    
print()
print(":: 전화번호 phone_book3[keys]로 접근하여 출력 ::")
for key in phone_book3.keys() :
    print(key, ":", phone_book3[key])
    
print()

print("딕셔너리 작성 시 :(콜론)을 기준으로 key:value 작성")
person__dict = {'name' : '임영훈', 'age' : 19, 'class' : '1학년'}

print('name :', person__dict['name'])   # 딕셔너리의 'name' 키로 값을 조회하여 출력
print('나이 :', person__dict['age'])   # 딕셔너리의 'age' 키로 값을 조회하여 출력

print()

print(":: 정렬 :: ")
# phone_book3 wjdfuf
print(sorted(phone_book3))

print(':: 키를 기준으로 전체 정렬 :: ')
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0])
print(sort_phone_book3)
print(':: 값을 기준으로 전체 정렬 :: ')
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1])
print(sort_phone_book3)

print()

print(':: 항목 삭제 ::')
del phone_book3['임영훈']
print(phone_book3)

print(":: 전체 삭제 ::")
phone_book3.clear()
print(phone_book3)
