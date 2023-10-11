'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.
    
    리스트에 10개의 값을 랜덤으로 생성하고,
    max 또는 min을 입력 받아 최대, 최소값을 찾아 돌려주는 함수
    
    (함수)
            5) 두 값을 전달받아 매개변수에 저장.
            6) 최대값, 최소값을 찾는다.
            7) 값을 돌려준다.
    (메인)
        1. 무한반복
            1) 랜덤으로 10~99까지 10개의 숫를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
                사용자가 입력하 값은 max 또는 min
            4) 입력받은 max 또는 min 과 생성된 리스트를 가지고 함수 호출
            8) 돌려 받은 최대값 또는 최소값을 출력한다.
'''

from random import randint

def getMinMax(lab_list, maxmin):
    if maxmin == 'max' :
        for i in (lab_list) :
            if i > lab_list :
                max = i
                
while True :
    lab_list = []
    for i in range(10):
        lab_list.append(randint(10,99))
    print(lab_list)
    maxmin = input("최대값 or 최솟값(max 또는 min으로 입력) = ")
    if maxmin == ['max','min'] :
        continue
    print("{}값은 {}입니다.".format(maxmin,getMinMax(lab_list,maxmin)))