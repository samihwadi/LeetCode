class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # We need n * '(' and n * ')'
        # Base cases are :=
        # n == '(' == ')'
        # ')' count < '(' count
        stack = []
        result = []
        def backtrack(open_count, close_count):
            if open_count == close_count == n:
                result.append("".join(stack))
                return
            if open_count < n:
                stack.append("(")
                backtrack(open_count + 1, close_count)
                stack.pop()
            if close_count < open_count:
                stack.append(")")
                backtrack(open_count, close_count + 1)
                stack.pop()
        backtrack(0, 0)
        return result
        
        