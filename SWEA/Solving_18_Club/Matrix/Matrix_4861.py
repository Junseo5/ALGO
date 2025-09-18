# 4861 . [파이썬 S/W 문제해결 기본] 3일차 - 회문

# i는 모든값 순회, j는 m-1부터 시작, n까지 순회
# 가로값 비교시 [i][j] 세로값 비교시 [j][i]
# j는 m-1부터 시작했으므로 j값부터 j-m까지 슬라이싱하여 회문 비교

tc = int(input())

for T in range(tc):
    n, m = map(int, input().split())

    n_list = [list(map(str, input())) for _ in range(n)]

    result = False

    for i in range(n):
        for j in range(m-1, n):
            temp1 = []
            temp2 = []
            for k in range(j - m + 1, j + 1):
                temp1.append(n_list[i][k])
                temp2.append(n_list[k][i])
            reverse_temp1 = temp1[::-1]
            reverse_temp2 = temp2[::-1]

            if temp1 == reverse_temp1:
                result = temp1
                break
            elif temp2 == reverse_temp2:
                result = temp2
                break
        if result:
            break

    print(f"#{T + 1} {''.join(result)}")

