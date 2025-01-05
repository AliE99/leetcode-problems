from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(val=preorder[0])
        index_of_root = inorder.index(preorder[0])
        root.left = self.buildTree(
            preorder=preorder[1 : index_of_root + 1], inorder=inorder[:index_of_root]
        )
        root.right = self.buildTree(
            preorder=preorder[1 + index_of_root :], inorder=inorder[index_of_root + 1 :]
        )

        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]

print(Solution().buildTree(preorder, inorder))
