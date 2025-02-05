from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        def divide_and_conquer(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return

            mid = (left + right) // 2
            node = TreeNode(val=nums[mid])
            node.left = divide_and_conquer(left, mid - 1)
            node.right = divide_and_conquer(mid + 1, right)

            return node

        return divide_and_conquer(0, len(nums) - 1)


nums = [-10, -3, 0, 5, 9]
print(Solution().sortedArrayToBST(nums))
