# 1970 . 쉬운 거스름돈

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
        else:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)

    def inorder_descending(self):
        result = []
        self._inorder_desc_recursive(self.root, result)
        return result

    def _inorder_desc_recursive(self, node, result):
        if node:
            self._inorder_desc_recursive(node.right, result)
            result.append(node.value)
            self._inorder_desc_recursive(node.left, result)


bst = BST()
denominations = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for denom in denominations:
    bst.insert(denom)

sorted_denoms = bst.inorder_descending()

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    result = []

    for denom in sorted_denoms:
        count = N // denom
        result.append(count)
        N %= denom

    print(f"#{tc}")
    print(*result)