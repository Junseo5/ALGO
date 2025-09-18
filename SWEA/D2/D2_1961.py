# 숫자 배열 회전

tc = int(input())

for i in range(tc):
    n = int(input())
    list_n1 = []
    
    print(f"#{i+1}")
    
    for j in range(n):
        list_n1.append(list(input().split()))
    
    for j in range(n):
        for k in range(n-1, -1, -1):
            print(list_n1[k][j], end="")
        print(" ", end="")
        for k in range(n-1, -1, -1):
            nn = (n-1) - j
            print(list_n1[nn][k], end="")
        print(" ", end="")
        
        for k in range(n):
            nn = (n-1) - j
            print(list_n1[k][nn], end="")
        print("")
        
        