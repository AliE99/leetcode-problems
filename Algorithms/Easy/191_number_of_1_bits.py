class Solution:
    def hammingWeight(self, n: int) -> int:
        if n == 0:
            return 0

        num_of_ones: int = 0
        while n >= 2:
            if n % 2 == 1:
                num_of_ones += 1
            n = n // 2

        return num_of_ones + 1
