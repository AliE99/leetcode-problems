class Solution:
    def trailingZeroes(self, n: int) -> int:
        result: int = 0
        while n >= 5:
            q = n // 5

            result += q
            n = q

        return result
