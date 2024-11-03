from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        current = 0
        i, j = 0, len(height) - 1
        while i < j:
            max_area = self.max_area(height, i, j)
            current = max(current, max_area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return current

    def max_area(self, height, i, j):
        return min(height[i], height[j]) * (j - i)


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(Solution().maxArea(height))
