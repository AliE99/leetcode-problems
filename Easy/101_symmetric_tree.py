# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left: TreeNode = root.left
        right: TreeNode = root.right

        return self.__is_symmetric(left, right)

    def __is_symmetric(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        if left == None and right == None:
            return True
        if not left or not right:
            return False

        if left.val != right.val:
            return False

        p = self.__is_symmetric(left.left, right.right)
        q = self.__is_symmetric(left.right, right.left)

        return p and q


root = [1, 2, 2, 3, 4, 4, 3]
