class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        max_cons = 0
        for num in nums:
            cons = 1
            if num - 1 in nums:
                continue
            # It's a start of the sequence
            while num + 1 in nums:
                cons += 1
                num += 1
            max_cons = max(cons, max_cons)

        return max_cons


nums = [100, 4, 200, 1, 3, 2]
nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
print(Solution().longestConsecutive(nums))
