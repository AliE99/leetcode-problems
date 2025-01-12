class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
nums = [-1, 0, 3, 5, 9, 12]
target = 2
print(Solution().search(nums, target))
