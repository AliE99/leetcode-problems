from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
            if numbers[i] + numbers[j] > target:
                j -= 1
            if numbers[i] + numbers[j] < target:
                i += 1


numbers = [2, 7, 11, 15]
target = 9

numbers = [2, 3, 4]
target = 6

numbers = [-1, 0]
target = -1
print(Solution().twoSum(numbers, target))
