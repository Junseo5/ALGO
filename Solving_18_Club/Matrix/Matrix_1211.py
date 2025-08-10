# 1211 . [S/W 문제해결 기본] 2일차 - Ladder2

# 사다리 최단거리를 찾아라
# 100 * 100 크기 2차원 배열 사다리
# 첫번째 줄 값이 1인곳이 출발선
# 최단거리 찾고 출력은 시작점 인덱스 번호 출력
# 복수인 경우 가장 큰 인덱스 번호 출력

# 빈 리스트에 1인 인덱스 번호 역순으로 저장 해둠
# 탐색도 역순으로 탐색
# 새 리스트에 출발점 개수만큼 0 생성
# 이 또한 역순으로 순회하면서 1을 계속 더함
# 가장 작은 수 찾음 min()
# 그 수를 index()로 찾음
# 이미 역순 정렬이므로 가장 큰수의 인덱스 번호 출력됨

# 어차피 가로선이 연속해서 이어지는 경우는 없다
# 즉 우측이면 이전 인덱스, 좌측이면 이후인덱스까지 수를 + 하면 된다

# 내려가는 와중 양옆 -1 +1 탐색

# import sys
# sys.stdin = open("input.txt", "r", encoding="utf-8")


for T in range(10):
    n = int(input())
    size = 100
    n_list = [list(map(int, input().split())) for _ in range(size)]
    
    start_idx_list = []
    
    for i in range(size-1, -1, -1):  # len(n_list[0])와 size와 같은값 100*100배열
        if n_list[0][i] == 1:
            start_idx_list.append(i)
    
    base_cnt_list = [0] * len(start_idx_list)
    
    for i in range(len(start_idx_list)):  # 오른쪽에서 왼쪽으로 출발 지점 순회
        tracing_idx = i
        for j in range(size):  # 위에서 아래로 내려가면서 순회(두번째 인덱스 i로 고정 및 좌우 탐색)
            now_x_loc = start_idx_list[tracing_idx]
            base_cnt_list[i] += 1
            
            if now_x_loc != size - 1 and n_list[j][now_x_loc + 1] == 1:  # and 연산자 앞에 인덱스 검사로 뒤 조건은 인덱스 오류나지 않음
                base_cnt_list[i] += start_idx_list[tracing_idx - 1] - start_idx_list[tracing_idx]  # 이동한 인덱스 만큼 더함
                tracing_idx -= 1  # 현재 이동중인 인덱스를 이동한 라인으로 변경
            elif now_x_loc != 0 and n_list[j][now_x_loc - 1] == 1:
                base_cnt_list[i] += start_idx_list[tracing_idx] - start_idx_list[tracing_idx + 1]
                tracing_idx += 1

    # 최단거리의 인덱스를 구하고 처음 입력한 리스트에서 해당 인덱스 번호를 출력
    print(f"#{T + 1} {start_idx_list[base_cnt_list.index(min(base_cnt_list))]}")