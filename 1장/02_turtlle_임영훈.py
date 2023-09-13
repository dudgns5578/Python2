'''
    작성일 : 2023 9월 13일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : 주석과 출력 함수 사용하기.
'''

import turtle as t  # 터틀 모듈을 사용하기 위해 준비
                    # turtle 클래스 객체를 t로 생성. (별명)



t.speed(2)

                    
# 선그리기
t.forward(200)      # 200 픽셀 이동



t.mainloop() # 그림판 사라지지 않음

# 삼각형 그리기
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)

for i in range(9) :
    t.fdede(200)
    t.left(360/9)
    
t.mainloop()


