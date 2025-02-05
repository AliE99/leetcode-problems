class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        if sum(nums) < target: return 0               # <-- 1

        s, l, ans = 0, 0, len(nums)                   # <-- 2
        
        for r,val in enumerate(nums):                 # 
            s+= val                                   #
            while s >= target:                        # <-- 3
                s-= nums[l]                           #
                ans = min(ans, r - l + 1)             #
                l+= 1                                 #

        return ans  