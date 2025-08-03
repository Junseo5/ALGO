# 1285. 아름이의 돌 던지기 (풀고보니 문제가 C++ 전용이었음..)

tc = int(input())

for T in range(tc):
    n = int(input())
    score = list(map(int, input().split()))
    
    # 0에 가까운 승리자 변수 초기화
    winner = 100000  # 최대 10만 ~ -10만 사이
    cnt = 0
    for i in score:
        i_abs = abs(i)  # 절대값 abs() 함수로 마이너스 케이스 양수로 변환
        if winner == i_abs:
            cnt += 1
        elif winner > i_abs:
            winner = i_abs
            cnt = 1
    
    print(f"#{T+1} {winner} {cnt}")