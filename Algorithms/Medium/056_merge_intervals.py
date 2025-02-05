from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][-1] >= intervals[i + 1][0]:
                intervals[i][1] = (max(intervals[i][-1], intervals[i + 1][-1]),)
                del intervals[i + 1]
            else:
                i += 1

        return intervals


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1, 4], [0, 4]]
intervals = [[1, 4], [0, 1]]
intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]

print(Solution().merge(intervals))
