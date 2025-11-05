# 16811 . 당근 포장하기

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    c_list = list(sorted(map(int, input().split())))

    op = N // 2

    temp = N

    for i in range(1, N - 1):
        if i > op:
            break
        if c_list[i - 1] == c_list[i]:
            continue

        for j in range(i + 1, N):
            if (j - i) > op:
                break
            if (N - j) > op:
                continue
            if c_list[j - 1] == c_list[j]:
                continue

            len_S = i
            len_M = j - i
            len_L = N - j

            temp = min(temp, max(len_S, len_M, len_L) - min(len_S, len_M, len_L))

    if temp == N:
        result = -1
    else:
        result = temp
    print(f"#{tc} {result}")