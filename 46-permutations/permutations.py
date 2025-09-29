class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        def backtrack():
            # Base case
            if len(sol) == n:
                res.append(sol[:])
                return
            for i in nums:
                if i not in sol:
                    sol.append(i)
                    backtrack()
                    sol.pop()
        backtrack()
        return res
        