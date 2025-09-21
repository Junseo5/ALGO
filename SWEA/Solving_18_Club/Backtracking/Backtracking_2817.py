# 2817 . 부분 수열의 합

def find_subsets(idx, num_sum, num_sum_list):
    global result
    if num_sum == k:
        result.append(num_sum_list)
        return

    if num_sum >= k: return

    if idx == len(n_list): return

    find_subsets(idx+1, num_sum + n_list[idx], num_sum_list + [n_list[idx]])

    find_subsets(idx+1, num_sum, num_sum_list)

tc = int(input())

for T in range(tc):
    n, k = map(int, input().split())
    n_list = list(sorted(map(int, input().split())))
    
    result = []
    find_subsets(0, 0, [])
    
    print(f"#{T + 1} {len(result)}")