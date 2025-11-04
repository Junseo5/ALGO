# Silver 3 . 13305 주유소

# N = int(input())
# road_list = list(map(int, input().split()))
# price_list = list(map(int, input().split()))
# base_list = [0] + [float('inf')] * (N - 1)

# for i in range(N):
#     if i != 0 and price_list[i] >= price_list[i - 1]:
#         continue
#     for j in range(i, N - 1):
#         temp_w = price_list[i] * road_list[j]
#         if temp_w + base_list[j] < base_list[j + 1]:
#             base_list[j + 1] = temp_w + base_list[j]
#         else:
#             break

# print(base_list[-1])


N = int(input())
road_list = list(map(int, input().split()))
price_list = list(map(int, input().split()))

result = 0
temp_price = price_list[0]
temp_multi = road_list[0]
for i in range(1, N - 1):
    if price_list[i] >= temp_price:
        temp_multi += road_list[i]
        continue
    else:
        result += temp_price * temp_multi
        temp_price = price_list[i]
        temp_multi = road_list[i]

result += temp_price * temp_multi

print(result)