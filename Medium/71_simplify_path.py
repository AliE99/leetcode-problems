from typing import Deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = Deque()
        path = path.split("/")
        for p in path:
            if p == ".." and stack:
                stack.pop()
                continue
            elif p and p != ".." and p != ".":
                stack.append(p)

        print(stack)
        result = ""
        if not stack:
            return "/"

        while stack:
            result = f"/{stack.pop()}{result}"
        return result


path = "/home/user/Documents/../Pictures"
path = "/home//foo/"
path = "/../"
path = "/.../a/../b/c/../d/./"
print(Solution().simplifyPath(path))
