class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        keyboard = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def backtack(index: str, curr_str: str):
            if len(curr_str) == len(digits):
                result.append(curr_str)
                return

            for char in keyboard[digits[index]]:
                backtack(index + 1, curr_str + char)

        if digits:
            backtack(0, "")

        return result


digits = "23"
print(Solution().letterCombinations(digits))
