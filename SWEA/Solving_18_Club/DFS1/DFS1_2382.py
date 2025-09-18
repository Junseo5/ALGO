# 2382 . [모의 SW 역량테스트] 미생물 격리

# 딕셔너리에 좌표를 키로 저장
# 이동시 새 딕셔너리에 좌표만 키로해서 append
# 같은 좌표인 그룹끼리 개수 더한 후 가장 많은 방향으로 업데이트
# i, y 값이 0이거나 n-1이면 그룹 방향 변경 및 절반 삭제

from collections import defaultdict

tc = int(input())

for T in range(tc):
    # n: 보드 크기, m: 시간, k: 군집 수
    n, m, k = map(int, input().split())

    origin_dict = {}

    for i in range(k):
        # 0: 세로, 1: 가로, 2: 미생물, 3: 방향(1:상, 2:하, 3:좌, 4:우)
        input_list = list(map(int, input().split()))
        origin_dict[(input_list[0], input_list[1])] = (input_list[2], input_list[3])
    
    for i in range(m):
        new_dict = defaultdict(list)
        for j in origin_dict:
            x, y = j
            unit, vec = origin_dict[j]
            
            if vec == 1:
                x -= 1
            elif vec == 2:
                x += 1
            elif vec == 3:
                y -= 1
            elif vec == 4:
                y += 1
            
            if x == 0 or x == n - 1 or y == 0 or y == n - 1:
                unit //= 2
                if vec == 1:
                    vec = 2
                elif vec == 2:
                    vec = 1
                elif vec == 3:
                    vec = 4
                elif vec == 4:
                    vec = 3

            new_dict[(x, y)].append((unit, vec))
        
        origin_dict = {}
        for j in new_dict:
            if len(new_dict[j]) == 1:
                origin_dict[j] = new_dict[j][0]
                continue

            x, y = j
            new_dict[j].sort(reverse=True)
            vec = new_dict[j][0][1]
            
            unit = 0
            for cnt, _ in new_dict[j]:
                unit += cnt
            
            origin_dict[j] = (unit, vec)
    
    total = 0
    for _, value in origin_dict.items():
        total += value[0]

    print(f"#{T + 1} {total}")