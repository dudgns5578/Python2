'''
    작성일 : 2023 9월 27일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : 점수를 입력받아 학점을 출력하시오.
            90~100 : A학점
            80~89 : B학점
            70~79 : C학점
            60~69 : D학점
            0~59 : F학점
            
    알고리즘 : 1. 점수를 입력 받는다.
                2. 판단하여 출력한다.
'''

# 점수를 입력 받는다.
score = int(input("점수 입력 : "))

# 판단
# 이 코드는 논리 오류가 발생한다.
print("::: 첫 번째 성적처리 ::: ")
if score >= 90:
    print("축하합니다 A 학점입니다.")
elif score >= 80:
    print("축하합니다 B 학점입니다.")
elif score >= 70:
    print("축하합니다. C 학점입니다.")
elif score >= 60:
    print("아쉽지만 D 학점입니다.")
elif score <= 59:
    print("안타깝게도 F 학점입니다.")
else :
    print("점수를 잘못 입력하셨습니다.")

    # 정확한 범위를 지정하자. - 성적의 범위를 벗어나면 잘못된 점수 입력입니다.
    '''
    90 ~ 100 : A학점
    80 ~ 89 : B학점
    70 ~ 79 : C학점
    60 ~ 69 : D학점
    0 ~ 59 : F학점
    '''
print("::: 두 번째 성적처리 :::")
if (90 <= score <= 100) :
    print("A학점")
elif (score >= 80 and score <= 89) :
    print("B학점")
     
