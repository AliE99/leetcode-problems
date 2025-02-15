from typing import Optional
from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        result: list[int] = []
        bfs_with_level: dict = self.level_order_with_levels(root)
        for _, nodes in bfs_with_level.items():
            result.append(nodes[-1])
        return result

    def level_order_with_levels(self, root: TreeNode) -> dict:
        if not root:
            return []

        queue = deque([(root, 0)])
        result = defaultdict(list)

        while queue:
            current, level = queue.popleft()
            result[level].append(current.val)

            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))

        return result


class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        result = []

        queue = deque([root])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return result
