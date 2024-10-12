# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


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


def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=" ")
        in_order_traversal(root.right)


# Array representation of the binary tree
arr = [2, 1, 3]
n = len(arr)
root = None
root = insert_level_order(arr, root, 0, n)

in_order_traversal(root)

print("--------------------------")
new_root = Solution().invertTree(root)

in_order_traversal(new_root)
