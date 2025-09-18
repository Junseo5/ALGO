# 1232 . [S/W 문제해결 기본] 9일차 - 사칙연산

def treeserch(node, result_list):
    if len(n_dict[node]) == 2:
        treeserch(n_dict[node][1][0], result_list)
        treeserch(n_dict[node][1][1], result_list)
        result_list.append(n_dict[node][0])
    else:
        result_list.append(n_dict[node][0])

    if str(result_list[-1]) in '+-*/':
        temp = result_list.pop()
        if temp == '+':
            num = result_list.pop()
            result_list[-1] += num
        elif temp == '-':
            num = result_list.pop()
            result_list[-1] -= num
        elif temp == '*':
            num = result_list.pop()
            result_list[-1] *= num
        elif temp == '/':
            num = result_list.pop()
            result_list[-1] /= num


for T in range(10):
    n_dict = {}
    n = int(input())
    for i in range(n):
        n_list = input().split()

        if n_list[1] in '+-*/':
            n_dict[int(n_list[0])] = [n_list[1], (int(n_list[2]), int(n_list[3]))]
        else:
            n_dict[int(n_list[0])] = [int(n_list[1])]

    result = []
    treeserch(1, result)
    print(f"#{T + 1} {int(result[0])}")