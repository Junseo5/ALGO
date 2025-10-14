# 13547. 팔씨름

T = int(input())
for tc in range(1, T + 1):
    S = input().strip()
    win = S.count('o')
    remain = 15 - len(S)

    if win + remain >= 8:
        result = "YES"
    else:
        result = "NO"

    print(f"#{tc} {result}")
