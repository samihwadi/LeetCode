class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Default value is no other higher temp is 0
        res = [0] * len(temperatures)
        stack = [] # [temp, index]
        for i, t in enumerate(temperatures):
            # Check if top temp is lower
            while stack and t > stack[-1][0]:   
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI 
            stack.append((t, i))
        return res 
        