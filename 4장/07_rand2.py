'''
    작성일 : 2023 9월 20일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : 선택문 if~else
            random 을 이용한 가위바위보 게임
            
            random 함수로 생성도니 정수를 가지고 게임을 진행합니다.
            0 => 가위
            1 => 바위
            2 => 보
            
            두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다.
'''
# 1. 첫번째 플레이어의 이름을 입력하시오.
player1 = input("첫번째 플레이어의 이름을 입력하시오. : ")

# 2. 두번째 플레이어의 이름을 입력하시오.
player2 = input("첫번째 플레이어의 이름을 입력하시오. : ")


import random   # random 함수 가져오기.(포함시키기)

print(":: 가위 바위 보 게임 시작 ::")

num1 = random.randrange(3)     # 랜덤으로 0,1,2 생성

num2 = random.randrange(3)

# player1의 가위 바위 보 출력
print(player1, " : ", end='')

if num1 == 0 :
    print("가위")
if num1 == 1 :
    print("바위")
if num1 == 2 :
    print("보")
    
# player2의 가위 바위 보 출력
print(player2, " : ", end='')

if num2 == 0 :
    print("가위")
if num2 == 1 :
    print("바위")
if num2 == 2 :
    print("보")
    
if num1 == 0 and num2 == 2 :
    print("{}가 승리하였습니다 축하합니다!" .format(player1))

if num1 == 1 and num2 == 0 :
    print("{}가 승리하였습니다 축하합니다!" .format(player1))
    
if num1 == 2 and num2 == 1 :
    print("{}가 승리하였습니다 축하합니다!" .format(player1))
    
elif num1 == num2:
    print("비겼습니다!")
    
else :
    print("{}가 승리하였습니다 축하합니다!" .format(player2))
    