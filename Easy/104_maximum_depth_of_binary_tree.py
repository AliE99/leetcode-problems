# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)

    def traverse(self, root: TreeNode, max_depth=0):
        if not root:
            return max_depth

        max_depth += 1

        if not root.left and not root.right:
            return max_depth

        max_depth_left = self.traverse(root.left, max_depth)
        max_depth_right = self.traverse(root.right, max_depth)

        return max(max_depth_left, max_depth_right)


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

arr = [1, None, 2]
n = len(arr)
root = None
root = insert_level_order(arr, root, 0, n)

print(Solution().maxDepth(root))
