class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result: list[list[int]] = []

        def backtrack(start, res):
            if len(res) == k:
                result.append(res[:])
                return

            for i in range(start, n + 1):
                res.append(i)
                backtrack(i + 1, res)
                res.pop()

        backtrack(1, [])

        return result


n = 4
k = 2
print(Solution().combine(n, k))
