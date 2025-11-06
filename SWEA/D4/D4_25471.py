# 25471 . 약수 게임

result_list = []
T = int(input().strip())
for tc in range(1, T + 1):
    n = int(input().strip())
    if n % 2 == 1:
        result_list.append('B')
        continue
    if not (n & (n - 1)) == 0:
        result_list.append('A')
        continue
    k = 0
    while n > 1:
        n >>= 1
        k += 1
    result_list.append('B' if (k % 2 == 1) else 'A')

print('\n'.join(result_list))
