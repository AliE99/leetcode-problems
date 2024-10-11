from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return nums

        result = []
        tmp = []
        i = 0
        while i < len(nums):
            if i == 0:
                tmp.append(nums[i])
            elif nums[i] - nums[i - 1] == 1:
                tmp.append(nums[i])
            else:
                result.append(tmp)
                tmp = [nums[i]]
            i += 1
        result.append(tmp)

        return self.generate_result(result)

    def generate_result(self, my_list: list) -> List[str]:
        result = []
        for res in my_list:
            if len(res) == 1:
                result.append(f"{res[0]}")
            else:
                result.append(f"{res[0]}->{res[-1]}")
        return result


nums = [0, 1, 2, 4, 5, 7]
print(Solution().summaryRanges(nums))
