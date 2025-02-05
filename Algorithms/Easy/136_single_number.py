class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        xor_value = 0
        for i in range(len(nums)):
            xor_value = xor_value ^ nums[i]

        return xor_value
