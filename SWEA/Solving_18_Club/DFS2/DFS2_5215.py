# 5215 . 햄버거 다이어트

def dfs(graph, idx, visited, total_score, total_cal, l):
    if idx == len(graph):
        return total_score
    
    max_score = total_score
    
    if total_cal + graph[idx][1] <= l:
        max_score = max(max_score, dfs(graph, idx + 1, visited, total_score + graph[idx][0], total_cal + graph[idx][1], l))
    
    max_score = max(max_score, dfs(graph, idx + 1, visited, total_score, total_cal, l))
    
    return max_score

tc = int(input())

for T in range(tc):
    n, l = map(int, input().split())
    n_list = [tuple(map(int, input().split())) for _ in range(n)]
    
    result = dfs(n_list, 0, set(), 0, 0, l)
    print(f"#{T + 1} {result}")