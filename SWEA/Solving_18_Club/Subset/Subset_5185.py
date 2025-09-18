# 5185 . [파이썬 S/W 문제해결 구현] 1일차 - 이진수

tc = int(input())

for T in range(tc):
    n, hex_str = input().split()
    n = int(n)
    
    bin_origin_num = bin(int(hex_str, 16))
    bin_num = bin_origin_num[2:]
    
    print(f"#{T + 1} {'0' * ((n * 4) - len(bin_num))}{bin_num}")