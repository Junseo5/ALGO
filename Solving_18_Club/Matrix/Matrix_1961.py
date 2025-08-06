# 1961 . 숫자 배열 회전

tc = int(input())

for T in range(tc):
    n = int(input())
    n_list = [input().split() for _ in range(n)]
    
    print(f"#{T + 1}")
    
    for i in range(n):
        for j in range(n-1, -1, -1):
            print(n_list[j][i], end="")
        print(" ", end="")
        for j in range(n-1, -1, -1):
            temp = (n-1) - i
            print(n_list[temp][j], end="")
        print(" ", end="")
        
        for j in range(n):
            temp = (n-1) - i
            print(n_list[j][temp], end="")
        print("")