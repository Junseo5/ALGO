# 5789 . 현주의 상자 바꾸기

tc = int(input())

for T in range(tc):
    n, q = map(int, input().split())

    boxs = ['0'] * n

    for i in range(q):
        l, r = map(int, input().split())

        for j in range(l-1, r):
            boxs[j] = str(i+1)
    
    boxs_join = ' '.join(boxs)
    
    print(f"#{T + 1} {boxs_join}")