class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        i, j, longest = 0, 0, 1
        while j < len(s) - 1:
            if s[j + 1] not in s[i : j + 1]:
                j += 1
                longest = max(longest, (j + 1 - i))
            else:
                i += 1

        return longest


s: str = "abcabcbb"
s: str = "bbbbb"
s: str = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
