from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.in_order_traversal: list[int] = self.__in_order_traversal(root)

    def next(self) -> int:
        return self.in_order_traversal.pop(0)

    def hasNext(self) -> bool:
        if self.in_order_traversal:
            return True

        return False

    @staticmethod
    def __in_order_traversal(root: TreeNode) -> list[int]:
        result: list[int] = []

        def traverse(node: Optional[TreeNode]):
            if not node:
                return
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

        traverse(root)
        return result


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
