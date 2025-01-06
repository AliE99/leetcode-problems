from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = [root]
        result = []
        new_node = TreeNode(val=-1)
        head = new_node
        while stack:
            node = stack.pop()
            result.append(node.val)
            new_node.right = node
            new_node.left = None
            new_node = new_node.right

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        root = head.right


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


arr = [1, 2, 5, 3, 4, None, 6]


root = None
root = insert_level_order(arr, root, 0, len(arr))

print(Solution().flatten(root))
