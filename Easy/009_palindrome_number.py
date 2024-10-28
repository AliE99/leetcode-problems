class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if len(x) == 1:
            return True
        i, j = 0, len(x) - 1
        while i < j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1

        return True


print(Solution().isPalindrome(121))
