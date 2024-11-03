class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True

        if len(s) == len(t) and s != t:
            return False

        i = j = 0
        while i < len(t):
            if t[i] != s[j]:
                i += 1
            else:
                i += 1
                j += 1
            if j == len(s):
                return True

        return False


s = "abc"
t = "ahbgdc"

s = ""
t = "ahbgdc"
print(Solution().isSubsequence(s, t))
