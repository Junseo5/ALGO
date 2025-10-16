# Gold 1 . 2042 구간 합 구하기

# N개의 수가 있는데 중간에 수의 변경이 빈번히 일어남
# 중간에 어떤 부분의 합을 구하려 함
# 1,2,3,4,5 중 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하면
# 17이 됨 2 + 6 + 4 + 5
# 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하면 6 + 4 + 2 = 12

from collections import defaultdict

result_list = []
N, M, K = map(int, input().split())
N_dict = {}
N10_dict = defaultdict(int)
N100_dict = defaultdict(int)
N1000_dict = defaultdict(int)
for i in range(1, N + 1):
    N_dict[i] = int(input().strip())
    N10_dict[i // 10] += N_dict[i]
    N100_dict[i // 100] += N_dict[i]
    N1000_dict[i // 1000] += N_dict[i]

for i in range((N + M + K + 1) - (N + 1)):
    a, b, c = map(int, input().split())

    if a == 1:
        N10_dict[b // 10] += (c - N_dict[b])
        N100_dict[b // 100] += (c - N_dict[b])
        N1000_dict[b // 1000] += (c - N_dict[b])
        N_dict[b] = c
    else:
        result = 0
        cnt = c - b + 1
        temp = b
        while cnt:
            if temp % 1000 == 0 and cnt >= 1000:
                result += N1000_dict[temp // 1000]
                cnt -= 1000
                temp += 1000
            elif temp % 100 == 0 and cnt >= 100:
                result += N100_dict[temp // 100]
                cnt -= 100
                temp += 100
            elif temp % 10 == 0 and cnt >= 10:
                result += N10_dict[temp // 10]
                cnt -= 10
                temp += 10
            else:
                result += N_dict[temp]
                cnt -= 1
                temp += 1

        result_list.append(f"{result}\n")

print(''.join(result_list))