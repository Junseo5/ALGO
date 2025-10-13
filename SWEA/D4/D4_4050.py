# 4050. 재관이의 대량 할인

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    n_list = list(sorted(map(int, input().split()), reverse=True))

    total = 0
    for i in range(N):
        if (i + 1) % 3 != 0:
            total += n_list[i]

    print(f"#{tc} {total}")
