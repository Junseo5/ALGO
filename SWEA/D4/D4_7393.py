# 7393. 대규의 팬덤활동

# 비트마스크 + DP로 문제 해결

MOD = 10**9
FULL = (1<<10) - 1  # 1023

T = int(input().strip())
for tc in range(1, T+1):
    N = int(input().strip())
    # 길이가 N인데 N < 10이면 모든 숫자(0~9)를 다 쓰는건 불가능
    if N < 10:
        print(f"#{tc} 0")
        continue

    # dp[d][mask] : 현재 끝자리가 d, 등장한 숫자 집합이 mask 인 경우의 수 (길이는 현재 pos)
    # 롤링 배열: pos = 1 초기화
    dp = [ [0]* (1<<10) for _ in range(10) ]
    for d in range(1, 10):  # 수는 0으로 시작할 수 없다
        dp[d][1<<d] = 1

    for pos in range(1, N):  # 이미 길이 1 초기화했으므로 N-1번 전이
        nxt = [ [0]* (1<<10) for _ in range(10) ]
        for d in range(10):
            arr = dp[d]
            if not any(arr):
                continue
            # 가능한 다음 자리: d-1, d+1 (유효 범위 체크)
            for mask in range(1<<10):
                v = arr[mask]
                if v == 0:
                    continue
                if d-1 >= 0:
                    nd = d-1
                    nmask = mask | (1<<nd)
                    nxt[nd][nmask] = (nxt[nd][nmask] + v) % MOD
                if d+1 <= 9:
                    nd = d+1
                    nmask = mask | (1<<nd)
                    nxt[nd][nmask] = (nxt[nd][nmask] + v) % MOD
        dp = nxt

    ans = 0
    for d in range(10):
        ans = (ans + dp[d][FULL]) % MOD

    print(f"#{tc} {ans}")