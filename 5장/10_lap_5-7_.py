'''
작성일 : 2023년 10월 04일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 단을 입력 받아 해당 단의 구구단을 출력하시오.
        교제 130pg
        
        문제 분석 : 원하는 단을 입력받는다.
        곱하는 수는 1~9까지이다.
        곱하는 수 시작 값 : 1
        곱하는 수 종료 값 : 9
        곱하는 수 증가 값 : 1
        
        필요한 변수 : dan , i
'''
# 단을 입력 받는다.
dan  = int(input("원하는 단을 입력하세요. : "))

# 곱하는 수는 1부터
i = 1 

# 곱하는 수를 9까지 반복하면서 
while i <= 9 :
    print("{} X {} = {}" .format(dan, i, dan*i))
    i = i + 1   # 곱하는 수 1 증가