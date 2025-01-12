class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        large_negative_number = -(
            1 << 31
        )  # Using left shift to create 2^31 and then negating it
        nums.insert(0, large_negative_number)
        nums.append(large_negative_number)

        low = 0
        high = len(nums) - 1

        while high >= low:
            mid = (high + low) // 2
            if max(nums[mid], nums[mid - 1], nums[mid + 1]) == nums[mid]:
                return mid - 1

            elif nums[mid - 1] > nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return mid - 1
