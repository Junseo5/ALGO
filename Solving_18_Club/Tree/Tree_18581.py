# 18581 . 이진트리-순회_실습

from collections import defaultdict


def preorder_traversal(current_node, result):
    if current_node:
        result.append(current_node)
        if len(n_dict[current_node]) == 2:
            preorder_traversal(n_dict[current_node][0], result)
            preorder_traversal(n_dict[current_node][1], result)
        elif len(n_dict[current_node]) == 1:
            preorder_traversal(n_dict[current_node][0], result)
    return result

def inorder_traversal(current_node, result):
    if current_node:
        if len(n_dict[current_node]) == 2:
            inorder_traversal(n_dict[current_node][0], result)
            result.append(current_node)
            inorder_traversal(n_dict[current_node][1], result)
        elif len(n_dict[current_node]) == 1:
            inorder_traversal(n_dict[current_node][0], result)
            result.append(current_node)
        else:
            result.append(current_node)
    return result


def postorder_traversal(current_node, result):
    if current_node:
        if len(n_dict[current_node]) == 2:
            postorder_traversal(n_dict[current_node][0], result)
            postorder_traversal(n_dict[current_node][1], result)
        elif len(n_dict[current_node]) == 1:
            postorder_traversal(n_dict[current_node][0], result)
        result.append(current_node)
    return result


v = int(input())
n_list = list(map(int, input().split()))
n_dict = defaultdict(list)

for i in range(1, len(n_list), 2):
    n_dict[n_list[i - 1]].append(n_list[i])

print(*preorder_traversal(n_list[0], []), '')
print(*inorder_traversal(n_list[0], []), '')
print(*postorder_traversal(n_list[0], []), '')

