from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff = 10**5
        stack = []
        current = root
        prev = None

        while current is not None or stack:
            # Reach the leftmost node of the current node
            while current is not None:
                stack.append(current)
                current = current.left

            # Current must be None at this point
            current = stack.pop()
            if prev:
                min_diff = min(min_diff, abs(current.val - prev.val))

            # Visit the right subtree
            prev = current
            current = current.right

        return min_diff
