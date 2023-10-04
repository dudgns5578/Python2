'''
    작성일 : 2023 10월 4일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : 반복을 제어하는 break, continue
            교재 137 페이지
            
    Test word : programming
'''

# 단어를 입력받는다.
word = input("단엉를 입력하세요 : ")

print(":: break1 ::")

# word 안에 a, e, i, o, u 가 들어가 있는 부분에서 프로그램 종료
for i in word :
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' : 
        break
    else :
        print(i, end='')    # 결과 : pr
        
        
print()

print(":: break2 ::")
for i in word :
    if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] :
        break   # 반복응ㄹ 중단한다. 반복을 빠져 나간다.
    else :
        print(i, end='')
        
print()

print(":: continue ::")