'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : 한번 생성하면 그 값을 고칠 수 없는 자료형 : 튜플
'''
# 리스트 생성
color_list = {'red', 'green', 'blue', 'orange'}
# 튜플 생성
color = ['red', 'green', 'blue', 'orange']

print(f"color : {color}")

# color에 black 추가하기
# AttributeError: 'tuple' object has no attribute 'append'
# AttributeError: 'tuple' 개체에 'append' 속성이 없습니다.
# 튜플은 추가, 삭제가 안된다.

# 인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.
print('color 튜플 : ', color)
print('color 튜플 중 2,3,4번은? ', color[1:4])
print('color 튜플 중 1,2,3번은? ', color[:3])
print('color 튜플 중 3,4 ~ 끝은? ', color[2:])
print('color 튜플 중 1,3,5번은? ', color[::2])
print('color 튜플 거꾸로 출력 ', color[::-1])

# 튜플 끼리의 결합 => + 연산자. 반복 => * 연산자
colors = color + color
print('colors 튜플 : ', colors)
print(f'color')
color.append('black')

