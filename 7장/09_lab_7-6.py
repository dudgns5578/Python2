'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터 공학부 202395027 임영훈
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''
# 다음과 같은 리스트가 생성되어 있다.

# 도시 정보를 리스트로 표현한다.
city_info = [('서울', 9765), ('부산', 3441), ('인천', 2954), ('광주', 1501), ('대전', 1531)]

# 최대 인구와 최소 인구를 초기값으로 설정한다.
max_population = city_info[0][1]       # 초기값을 0으로 설정하면, 이 변수가 첫 번째 도시의 인구와 비교될 때,
                         # 첫 번째 도시의 인구가 현재까지의 최대 인구로 설정됩니다.
                         
min_population = city_info[0][1]
                         #첫 번째 도시의 인구와 비교될 때, 첫 번째 도시의 인구가 
                         # 현재까지의 최소 인구로 설정될 수 있도록 하기 위함입니다.

# 전체 도시 인구의 합을 저장할 변수 초기화
total_population = 0

# 최대 인구를 가진 도시와 최소 인구를 가진 도시의 정보를 저장할 변수 초기화
max_city = city_info[0][1]
min_city = city_info[0][1]

# 각 도시 정보를 순회하며 처리
for city, population in city_info:
    total_population += population  # 도시 인구를 더하여 전체 인구 합을 계산
    
    # 최대 인구 도시 정보 업데이트
    if city[1] > max_population:
        max_population = city[1]
        max_city = city
    
    # 최소 인구 도시 정보 업데이트
    if city[1] < min_population:
        min_population = city[1]
        min_city = city

# 최대 인구 도시와 최소 인구 도시 정보 출력
print('최대인구: {}, 인구: {} 천명'.format(max_city[0], max_population))
print('최소인구: {}, 인구: {} 천명'.format(min_city[0], min_city[1]))

# 리스트의 도시들의 평균 인구 출력
print('리스트 도시 평균 인구: {} 천명'.format(total_population / len(city_info)))
