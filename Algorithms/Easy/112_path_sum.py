from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum

        left_sum = self.hasPathSum(root=root.left, targetSum=targetSum - root.val)
        right_sum = self.hasPathSum(root=root.right, targetSum=targetSum - root.val)

        return left_sum or right_sum
