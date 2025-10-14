class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_pair = {
            "]":"[",
            ")":"(",
            "}":"{"
        }
        for b in s:
            if b in close_open_pair:
                if stack and stack[-1] == close_open_pair[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        if not stack:
            return True
        return False