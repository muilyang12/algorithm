class Solution:
    def simplifyPath(self, path: str) -> str:
        pathes = path.split("/")

        stack = []
        for p in pathes:
            if p == "" or p == ".":
                continue
            elif p == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(p)

        return "/" + "/".join(stack)
