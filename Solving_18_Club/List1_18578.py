# 18578 . Gravity_실습

tc = int(input())

for T in range(tc):
    n = int(input())
    boxs = list(map(int, input().split()))

    result = boxs[0]
    cnt = 0

    for i in range(len(boxs)):
        if result > boxs[i]:
            cnt += 1
        elif cnt < 1:
            result = boxs[i]
        
    print(f"#{T+1} {cnt}")
