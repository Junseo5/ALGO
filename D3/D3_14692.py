# 14692. 통나무 자르기

tc = int(input())

for T in range(tc):
    n = int(input())
    print(f"#{T + 1} {'Alice' if n % 2 == 0 else 'Bob'}")