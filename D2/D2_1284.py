# 1284. 수도 요금 경쟁

tc = int(input())

for T in range(tc):
    p, q, r, s, w = map(int, input().split()) # 8 300 100 10 250

    over = 0

    if w > r:
        over = w - r

    if w * p < q + (over * s):
        total_price = w * p
    else:
        total_price = q + (over * s)
    
    print(f"#{T+1} {total_price}")