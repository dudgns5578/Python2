'''
    작성일 : 2023 9월 20일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : 선택문 if~else
            정수를 입력받아 짝수인지 홀수인지 판단.
            
            짝수 = 2로 나눈 나머지가 0이다.
            홀수 = 2로 나눈 나머지가 1이다. (0이 아니다.)
'''

# 1. 정수를 입력 받는다.
num = int(input("정수를 입력하시오 : "))

# 2. 2로 나눈 나머지가 0이라면 짝수입니다. 출력
if num % 2 == 0:
    print("{} 은(는) 짝수입니다." .format(num))

# 2.1. 그게 아니면 홀수입니다. 출력
else:
    print("{} 은(는) 홀수입니다." .format(num))