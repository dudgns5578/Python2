'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : 리스트에서 사용 가능한 함수
'''
population = ['Seoul', 9765, 'Busan', 3441, 'Incheon', 2954]

# 1) 서울의 인구(두 번째 요소) 출력
seoul_population = population[1]
print("서울 인구:", seoul_population)

# 2) 인천의 인구(마지막 요소, 음수 인덱스 사용)
incheon_population = population[-1]
print("인천 인구:", incheon_population)

# 3) 각 도시의 이름을 step 값을 이용하여 출력
step = 2  # 도시 이름과 인구가 번갈아 나오므로 2칸씩 이동
city_names = population[0::step]
print("도시 리스트:", city_names)

# 4) 각 도시의 인구를 step 값을 이용하여 출력하고 합 출력
step = 2  # 도시 이름과 인구가 번갈아 나오므로 2칸씩 이동
total_population = sum(population[1::step])  # 인구 값들은 짝수 인덱스에 있음
print("인구의 합:", total_population)
