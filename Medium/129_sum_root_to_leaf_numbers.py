from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def calc_result(root: Optional[TreeNode], result: str):
            if not root:
                return ""

            result += f"{root.val}"
            if not root.left and not root.right:
                final_result.append(int(result))

            calc_result(root.left, result)
            calc_result(root.right, result)

            return result

        final_result = []
        calc_result(root, "")
        return sum(final_result)
