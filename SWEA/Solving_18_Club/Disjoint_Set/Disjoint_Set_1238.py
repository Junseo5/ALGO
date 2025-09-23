# 1238 . [S/W 문제해결 기본] 10일차 - Contact

from collections import defaultdict, deque

tc = 10
for T in range(tc):
    n, start = map(int, input().split())
    origin_list = list(map(int, input().split()))

    graph = defaultdict(list)

    for i in range(0, len(origin_list), 2):
        from_node = origin_list[i]
        to_node = origin_list[i + 1]

        if to_node not in graph[from_node]:
            graph[from_node].append(to_node)

    queue = deque([start])
    visited = {start}
    max_time = 0
    time_dict = {start: 0}

    while queue:
        current = queue.popleft()
        current_time = time_dict[current]

        for next_person in graph[current]:
            if next_person not in visited:
                visited.add(next_person)
                queue.append(next_person)
                time_dict[next_person] = current_time + 1
                max_time = max(max_time, current_time + 1)

    max_number = 0
    for person, time in time_dict.items():
        if time == max_time:
            max_number = max(max_number, person)

    print(f"#{T + 1} {max_number}")