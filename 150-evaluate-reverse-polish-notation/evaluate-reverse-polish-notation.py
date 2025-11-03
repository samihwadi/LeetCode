class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()
                match char:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case _:
                        stack.append(int(a/b))
            else:
                stack.append(int(char))           
        return int(stack[0])