# 14555. 공과 잡초

T = int(input())
for tc in range(1, T + 1):
    S = input()

    cnt = 0
    temp = ''
    for ch in S:
        if ch == '|' and temp == '(':
            cnt += 1
        elif ch == ')':
            if temp == '|':
                cnt += 1
            elif temp == '(':
                cnt += 1
        temp = ch

    print(f"#{tc} {cnt}")