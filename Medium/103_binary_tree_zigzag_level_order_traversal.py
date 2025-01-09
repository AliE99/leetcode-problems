from typing import Optional
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        queue = deque([(root, 0)])
        result = defaultdict(list)

        while queue:
            node, level = queue.popleft()
            if level % 2 == 0:
                result[level].append(node.val)
            else:
                result[level].insert(0, node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return [value for _, value in result.items()]
