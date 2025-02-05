class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        i, j = 0, len(words) - 1

        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1

        return " ".join(words)


s = "the sky is blue"
s = "  hello world  "
s = "a good   example"
print(Solution().reverseWords(s))
