from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        maped = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        for parentheses in s:
            if parentheses in maped:
                stack.append(parentheses)
            elif not stack or maped[stack.pop()] != parentheses:
                return False

        return len(stack) == 0


s = "()[]{}"
s = "["
print(Solution().isValid(s))
