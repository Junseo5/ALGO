# 파리퇴치3

tc = int(input())

for i in range(tc):
    sum = 0
    n, nn = map(int, input().split())
    list_n1 = []
    for j in range(int(n)):
        n1 = input()
        list_n1.append(list(map(int, n1.split())))

    for j in range(int(n)):
        for k in range(int(n)):
            p = x = list_n1[j][k]
            for m in range(1, int(nn)):
                p += ((list_n1[j + m][k] if j+m < int(n) else 0) + (list_n1[j][k - m] if k-m >= 0 else 0) + (list_n1[j - m][k] if j-m >= 0 else 0) + (list_n1[j][k + m] if k+m < int(n) else 0))
                x += ((list_n1[j + m][k + m] if j+m < int(n) and k+m < int(n) else 0) + (list_n1[j + m][k - m] if j+m < int(n) and k-m >= 0 else 0) + (list_n1[j - m][k - m] if j-m >= 0 and k-m >= 0 else 0) + (list_n1[j - m][k + m] if j-m >= 0 and k+m < int(n) else 0))
            if p > sum or x > sum:
                if p > sum:
                    sum = p
                else:
                    sum = x
    print(f"#{i+1} {sum}")