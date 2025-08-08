# 1208 . [S/W 문제해결 기본] 1일차 - Flatten

# 가장 높은 상자 가장 낮은곳으로 덤프
# 덤프한 횟수 출력

# 가로 길이는 항상 100
# 모든 위치에서 상자의 높이는 1 이상 100 이하
# 덤프 횟수도 1이상 1000이하
# 주어진 덤프 횟수까지 돌고 최고 최저 높이차 반환

# 총 10개의 테스트 케이스 주어짐
# 첫번째줄 덤프 횟수 주어짐
# 두번째줄 각 상자의 높이값 주어짐

for T in range(10):
    n = int(input())
    n_list = list(map(int, input().split()))
    size = 100  # len(n_list)

    for i in range(n):
        max_idx = n_list.index(max(n_list))  # 가장 큰값의 인덱스
        min_idx = n_list.index(min(n_list))
        
        n_list[max_idx] -= 1
        n_list[min_idx] += 1
    
    print(f"#{T + 1} {max(n_list) - min(n_list)}")