from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(root: Optional[TreeNode]) -> list[int]:
    result = []

    def traverse(node: Optional[TreeNode]):
        if node is None:
            return
        traverse(node.left)
        result.append(node.val)
        traverse(node.right)

    traverse(root)
    return result
