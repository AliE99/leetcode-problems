from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def calc(root, num: int):
            if root == None:
                return 0

            num = num * 10 + root.val
            if not root.left and not root.right:
                return num

            return calc(root.left, num) + calc(root.right, num)

        return calc(root, 0)
