# 4008 . [모의 SW 역량테스트] 숫자 만들기

def dfs(depth, current_value, plus, minus, multiply, divide):
    global max_val, min_val, num_list, n

    if depth == n:
        max_val = max(max_val, current_value)
        min_val = min(min_val, current_value)
        return

    if plus > 0:
        dfs(depth + 1, current_value + num_list[depth], plus - 1, minus, multiply, divide)

    if minus > 0:
        dfs(depth + 1, current_value - num_list[depth], plus, minus - 1, multiply, divide)

    if multiply > 0:
        dfs(depth + 1, current_value * num_list[depth], plus, minus, multiply - 1, divide)

    if divide > 0:
        if current_value < 0:
            dfs(depth + 1, -(-current_value // num_list[depth]), plus, minus, multiply, divide - 1)
        else:
            dfs(depth + 1, current_value // num_list[depth], plus, minus, multiply, divide - 1)


tc = int(input())

for T in range(tc):
    n = int(input())
    operators = list(map(int, input().split()))
    num_list = list(map(int, input().split()))

    max_val = -100000000
    min_val = 100000000

    dfs(1, num_list[0], operators[0], operators[1], operators[2], operators[3])

    print(f"#{T + 1} {max_val - min_val}")