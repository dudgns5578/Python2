'''
    작성일 : 2023 9월 27일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : 터틀 그래픽으로 여러 개의 원을 그려보자.
'''

import turtle as t

# 원 하나 그리기
# t.circle(100)

for count in range(5) :
    t.circle(100)
    t.left(360 / 5)
    
t.mainloop()    # 종료