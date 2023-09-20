'''
    작성일 : 2023 9월 20일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : 선택문 if~else
            random 을 이용한 가위바위보 게임
            
            random 함수로 생성도니 정수를 가지고 게임을 진행합니다.
            0 => 가위
            1 => 바위
            2 => 보
'''

import random   # random 함수 가져오기.(포함시키기)

print(":: 가위 바위 보 게임 시작 ::")

random.randrange(3)     # 랜덤으로 0,1,2 생성

# 가위 바위 보 출력

if num == 1 :
    print("가위")
if num == 2 :
    print("바위")
if num == 3 :
    print("보")