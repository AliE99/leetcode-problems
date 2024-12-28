class Solution:
    def candy(self, ratings: list[int]) -> int:
        candy = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candy[i + 1] = candy[i] + 1

        i = len(ratings) - 1
        while i > 0:
            if ratings[i - 1] > ratings[i] and candy[i - 1] <= candy[i]:
                candy[i - 1] = candy[i] + 1
            i -= 1

        return sum(candy)


e = [1, 0, 2]
# e = [1, 2, 2]
# e = [1, 3, 2, 2, 1]
# e = [29, 51, 87, 87, 72, 12]
# e = [1, 3, 4, 5, 2]
print(Solution().candy(e))
