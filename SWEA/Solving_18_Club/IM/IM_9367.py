# 9367 . 점점 커지는 당근의 개수

# 순서대로 증가한 숫자의 개수를 구하라
# 전혀 증가하지 않으면 기본값 1

# import sys
# sys.stdin = open("input.txt", "r", encoding="utf-8")

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = list(map(int, input().split()))
    
    cnt = 1
    max_cnt = 1
    
    for i in range(1, n):  # 인덱스 비교를 위해 1부터 시작
        if n_list[i - 1] < n_list[i]:  # 현재값이 이전값보다 클 때
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 1
    
    print(f"#{T + 1} {max_cnt}")