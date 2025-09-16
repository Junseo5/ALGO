# 1231 . [S/W 문제해결 기본] 9일차 - 중위순회

def inorder(node, result):
    if node:
        if len(n_dict[node]) == 2:
            inorder(n_dict[node][1][0], result)
            result.append(n_dict[node][0])
            inorder(n_dict[node][1][1], result)
        else:
            result.append(n_dict[node][0])


for T in range(10):
    n = int(input())
    n_dict = {}

    for i in range(1, n + 1):
        n_list = input().split()

        if len(n_list) == 4:
            n_dict[i] = [n_list[1], (int(n_list[2]), int(n_list[3]))]
        elif len(n_list) == 3:
            n_dict[i] = [n_list[1], (int(n_list[2]), 0)]
        else:
            n_dict[i] = [n_list[1]]

    result = []
    inorder(1, result)

    print(f"#{T + 1} {''.join(result)}")