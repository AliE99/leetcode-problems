class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= nums[l] and nums[mid] <= nums[r]:
                if nums[mid] <= nums[mid - 1]:
                    return nums[mid]
                r = mid - 1
            elif nums[mid] < nums[r] and nums[mid] > nums[l]:
                r = mid - 1
            else:
                l = mid + 1

        return -1
