'''
작성일 : 2023년 10월 04일
학과 : 컴퓨터 공학부
학번 : 202395027   
이름 : 임영훈
설명 : 두 수를 입력받아
        1. 두 수 사이의 합계 출력하기
        2. 두 수 사이의 짝수의 합계 출력하기
        
        심호문제 5-2, 141pg
'''

while True:
    num1 = int(input("첫 번째 정수를 입력하세요: "))
    num2 = int(input("두 번째 정수를 입력하세요: "))

    if num1 < num2:
        break  # 올바른 입력인 경우 반복문을 종료합니다.
    else:
        print("잘못 입력하셨습니다. 첫 번째 숫자가 두 번째 숫자보다 작아야 합니다. 다시 입력하세요.")

# 두 수 사이의 합계를 계산
total_sum = 0
for i in range(num1, num2 + 1):
    total_sum += i

# 두 수 사이의 짝수의 합계를 계산
even_sum = 0
for i in range(num1, num2 + 1):
    if i % 2 == 0:
        even_sum += i

# 결과 출력
print(f"{num1}부터 {num2}까지의 합계는 {total_sum}입니다.")
print(f"{num1}부터 {num2}까지의 짝수의 합계는 {even_sum}입니다.")


