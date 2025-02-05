from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack: list[TreeNode] = []
        result: int = []
        current = root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if len(result) == k - 1:
                return current.val
            result.append(current.val)

            current = current.right

        return result[k - 1]
