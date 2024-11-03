import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        x = len(s)

        if s == "" or x == 1:
            return True

        for i in range(0, x):
            if i >= (x - i):
                return True

            if s[i] != s[x - i - 1]:
                return False


s: str = "A man, a plan, a canal: Panama"

print(Solution().isPalindrome(s))
