from typing import Optional
from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> list[float]:
        result: list[float] = []
        bfs_with_levels = self.level_order_with_levels(root)
        for _, node_vals in bfs_with_levels.items():
            result.append(sum(node_vals) / len(node_vals))

        return result

    def level_order_with_levels(self, root: TreeNode) -> dict:
        if not root:
            return {}

        queue = deque([(root, 0)])
        result = defaultdict(list)

        while queue:
            node, level = queue.popleft()
            result[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result


def insert_level_order(arr, root, i, n):
    # Base case for recursion
    if i < n:
        if arr[i] is not None:
            temp = TreeNode(val=arr[i])
            root = temp

            # insert left child
            root.left = insert_level_order(arr, root.left, 2 * i + 1, n)

            # insert right child
            root.right = insert_level_order(arr, root.right, 2 * i + 2, n)
    return root


# Array representation of the binary tree
# arr = [3, 9, 20, None, None, 15, 7]

arr = [3, 9, 20, None, None, 15, 7]
n = len(arr)
root = None
root = insert_level_order(arr, root, 0, n)

print(Solution().averageOfLevels(root))
