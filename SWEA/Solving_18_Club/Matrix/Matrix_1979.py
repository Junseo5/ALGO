# 1979 . 어디에 단어가 들어갈 수 있을까

tc = int(input())

for T in range(tc):
    n, k = map(int, input().split())
    n_list = [list(map(int, input().split())) for _ in range(n)]

    total_cnt = 0

    for i in range(n):
        cnt1 = 0
        save_cnt1 = -1
        cnt2 = 0
        save_cnt2 = -1
        for j in range(n):
            # 가로 단어 비교 및 카운트
            if n_list[i][j] == 1:
                cnt1 += 1
                if j == n-1:
                    save_cnt1 = cnt1
            elif n_list[i][j] == 0:
                save_cnt1 = cnt1
                cnt1 = 0
            # 세로 단어 비교 및 카운트
            if n_list[j][i] == 1:
                cnt2 += 1
                if j == n-1:
                    save_cnt2 = cnt2
            elif n_list[j][i] == 0:
                save_cnt2 = cnt2
                cnt2 = 0
            # 저장된 단어 카운팅
            if k == save_cnt1:
                total_cnt += 1
                save_cnt1 = -1
            if k == save_cnt2:
                total_cnt += 1
                save_cnt2 = -1

    print(f"#{T + 1} {total_cnt}")