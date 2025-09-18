# 23488 . 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

# 가장 적재량이 작은 화물차부터 가능한 화물중 가장 큰 화물 운반

# n_list를 내림차순, m_list를 오름차순 정렬 후
# m_list 순회하며 n_list 중 가능한 화물 탐색 후 total에 무게 더함

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())
    n_list = list(sorted(map(int, input().split()), reverse=True))
    m_list = list(sorted(map(int, input().split())))
    
    total = 0
    
    for i in range(m):
        if len(n_list) == 0:
            break
        
        if m_list[i] <= n_list[-1]:  # 시간 단축을 위한 최소한의 조건 처리
            if m_list[i] == n_list[-1]:
                total += n_list[-1]
                n_list.pop()
            continue
        
        for j in range(len(n_list)):
            if m_list[i] >= n_list[j]:
                total += n_list[j]
                n_list.pop(j)
                break
    
    print(f"#{T + 1} {total}")