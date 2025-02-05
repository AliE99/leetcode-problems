class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low = 0
        high = len(nums) - 1
        result = [-1, -1]
        while high >= low:
            mid = (high + low) // 2

            if nums[mid] == target:
                result = [mid, mid]
                i, j = mid - 1, mid + 1
                while i >= low or j <= high:
                    if nums[i] == nums[mid] and i >= low:
                        result[0] = i
                    if nums[j] == nums[mid] and j <= high:
                        result[1] = j
                    i -= 1
                    j += 1
                return result
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return result


nums = [2, 2]
print(Solution().searchRange(nums, 2))
