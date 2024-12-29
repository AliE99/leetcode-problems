class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag_chars: str = ""
        if numRows == 1:
            return s

        for r in range(numRows):
            jump = 2 * (numRows - 1)
            for i in range(r, len(s), jump):
                zigzag_chars += s[i]
                if r > 0 and r < numRows - 1 and i + jump - 2 * r < len(s):
                    zigzag_chars += s[i + jump - 2 * r]

        return zigzag_chars


s = "PAYPALISHIRING"

print(Solution().convert(s=s, numRows=3))
