'''
작성일 : 2023년 10월 04일
학과 : 컴퓨터 공학부
학번 : 202395032   
이름 : 최민호
설명 : 조건에 따라 반복하는 whlie 문
        교제 128pg
        
        사용자로부터 계속해서 암호를 입력 받는다.
        암호가 맞으면 로그린 성공 매세지를 출력한다.
        암호가 맞을 떄까지 반복한다.
        암호는 1234
        
        암호가 1234가 아니면 계속 암호를 입력하라고 한다.
'''

pw = ""

while pw != "1234" :
        pw = input("암호를 입력하세요. : ")
print("로그인 성공! ")