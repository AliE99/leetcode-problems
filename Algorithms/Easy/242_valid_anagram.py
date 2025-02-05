from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if set(s) != set(t):
            return False

        map_s = {}
        map_t = {}
        for i in range(0, len(s)):
            if s[i] in map_s:
                map_s[s[i]] += 1
            else:
                map_s[s[i]] = 1

            if t[i] in map_t:
                map_t[t[i]] += 1
            else:
                map_t[t[i]] = 1

        if map_s != map_t:
            return False

        return True


s = "anagram"
t = "nagaram"

s = "aacc"
t = "ccac"

print(Solution().isAnagram(s, t))


class PythonicSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        if counter_s == counter_t:
            return True

        return False


s = "anagram"
t = "nagaram"
print(PythonicSolution().isAnagram(s, t))
