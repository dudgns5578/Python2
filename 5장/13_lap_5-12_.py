'''
작성일 : 2023년 10월 04일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 더하기 암산 문제 만들기
        2개의 수로 더하기 결과를 맞추는 게임.
        2개의 수는 1~100사이 램덤츠로 출제 됨.
        
        사용자가 0을 입력하면 프로그램 종료
        즉, 사용자가 0을 입력하기 전까지는 무한 반복하여 문제 출기
        정답을 맞추면 "참 잘했어요." 출력
        틀리면 정답을 알려주고 "틀렸습니다." 출력
'''

import random

while True :
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    print("{} + {} = ?".format(num1,num2,))
    total = int(input("정답 입력 : "))
    if total == num1+num2 :
        print("정답입니다. (종료키 0)")
    elif total == 0 :
        break    
    else :
        print("틀렸습니다. {} + {} = {}입니다.".format(num1,num2,num1+num2))