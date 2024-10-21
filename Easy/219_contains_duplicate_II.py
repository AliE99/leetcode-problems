from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_map = dict()
        i = 0
        while i < len(nums):
            if nums[i] not in my_map:
                my_map[nums[i]] = i
            else:
                j = my_map[nums[i]]
                if abs(j - i) <= k:
                    return True
                else:
                    my_map[nums[i]] = i
            i += 1

        return False


nums = [1, 2, 3, 1]
k = 3

nums = [1, 0, 1, 1]
k = 1
print(Solution().containsNearbyDuplicate(nums, k))
