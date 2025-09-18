# 3143 . 가장 빠른 문자열 타이핑

tc = int(input())

for T in range(tc):
    a, b = map(str, input().split())
    a_list = list(a)

    cnt = 0
    
    while a_list:
        b_idx = ''.join(a_list).find(b)
        if b_idx == -1:
            cnt += len(a_list)
            break
        else:
            del a_list[b_idx:b_idx+len(b)]
            cnt += 1

    print(f"#{T + 1} {cnt}")