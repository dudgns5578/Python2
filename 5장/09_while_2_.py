'''
작성일 : 2023년 10월 04일
학과 : 컴퓨터 공학부
학번 : 202395027   
이름 : 임영훈
설명 : 조건에 따라 반복하는 whlie 문
        교제 129pg
        
        1~10까지의 함계를 계산하여 출력하기
        시작 값 : 1 
        종료 값 : 10
        증가 값 : 1
        for i in rnage(1,11) => while 문으로
        
        필요한 변수 : count, s  
'''

count = 1 # 시작 값
s = 0   # 합계 계산을 위한 초기값 지정.

while count <= 10 :     # 종료 값 (조건식)
    s = s + count    # 합계 계산
    count = count + 1 # 증가 값

print("합계 : ", s)