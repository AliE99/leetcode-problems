class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(nums: list[int], curr_result: list[int]):
            if len(curr_result) == len(nums):
                result.append(curr_result[:])
                return

            for i in range(len(nums)):
                if nums[i] in curr_result:
                    continue
                curr_result.append(nums[i])
                backtrack(nums, curr_result)
                curr_result.pop()

        backtrack(nums, [])
        return result


nums = [1, 2, 3]
print(Solution().permute(nums))
