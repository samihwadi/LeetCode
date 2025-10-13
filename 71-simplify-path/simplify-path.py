class Solution:
    def simplifyPath(self, path: str) -> str:
        # Using a stack to add the valid directories to path
        stack = []
        curr = ""
        for char in path + '/':
            if char == '/':
                # Previous directory so pop current directory if present
                if curr == '..':
                    if stack:
                        stack.pop()
                elif curr != "" and curr != '.':
                    stack.append(curr)
                curr = ""
            else:
                curr += char
        return '/' + '/'.join(stack)

            
        