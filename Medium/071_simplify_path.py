class Solution:
    def simplifyPath(self, path: str) -> str:
        directory = []
        path = path.split("/")
        for p in path:
            if directory and p == "..":
                directory.pop()
            elif p not in ["", ".", ".."]:
                directory.append(p)

        return "/" + "/".join(directory)


path = "/home/user/Documents/../Pictures"
path = "/home//foo/"
path = "/../"
path = "/.../a/../b/c/../d/./"
print(Solution().simplifyPath(path))
