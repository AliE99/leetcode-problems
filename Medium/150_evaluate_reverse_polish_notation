class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                num1 = stack.pop()
                num2 = stack.pop()
                result = f"{num2}{token}{num1}"
                stack.append(int(eval(result)))
            else:
                stack.append(int(token))

        return stack[0]


tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(tokens))
