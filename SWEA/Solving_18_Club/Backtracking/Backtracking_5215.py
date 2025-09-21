# 5215 . 햄버거 다이어트

def backtracking(graph, idx, total_score, total_cal, l):
    global best
    
    if total_cal > l:
        return
    
    if idx == len(graph):
        best = max(best, total_score)
        return
    
    best = max(best, total_score)
    
    score, cal = graph[idx]
    backtracking(graph, idx + 1, total_score + score, total_cal + cal, l)
    
    backtracking(graph, idx + 1, total_score, total_cal, l)


tc = int(input())
for T in range(tc):
    n, l = map(int, input().split())
    n_list = [tuple(map(int, input().split())) for _ in range(n)]
    
    best = 0
    backtracking(n_list, 0, 0, 0, l)
    
    print(f"#{T + 1} {best}")
