# 1989 . 초심자의 회문 검사

T = int(input())

for tc in range(1, T + 1):
    n = input().strip()

    print(f"#{tc} {1 if n == n[-1::-1] else 0}")