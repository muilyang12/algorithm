class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        typed_s = []
        for char in s:
            if char != "#":
                typed_s.append(char)
            elif char == "#" and typed_s:
                typed_s.pop()

        typed_t = []
        for char in t:
            if char != "#":
                typed_t.append(char)
            elif char == "#" and typed_t:
                typed_t.pop()

        return "".join(typed_s) == "".join(typed_t)
