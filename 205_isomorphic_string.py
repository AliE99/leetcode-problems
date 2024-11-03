class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False

        my_map = {}
        for i in range(len(s)):
            if s[i] in my_map and my_map[s[i]] != t[i]:
                return False

            my_map[s[i]] = t[i]

        return True



s = "egg"
t = "add"

s = "badc"
t = "baba"
print(Solution().isIsomorphic(s, t))
