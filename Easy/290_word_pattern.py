class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False

        if len(set(s)) != len(set(pattern)):
            return False

        my_map = {}
        i = 0
        for i in range(0, len(pattern)):
            if s[i] in my_map and my_map[s[i]] != pattern[i]:
                return False
            my_map[s[i]] = pattern[i]
        return True


pattern = "abba"
s = "dog cat cat dog"
# s = "dog dog dog dog"
print(Solution().wordPattern(pattern, s))
