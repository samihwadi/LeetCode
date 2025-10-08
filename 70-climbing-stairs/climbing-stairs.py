class Solution:
    def climbStairs(self, n: int) -> int:
        # Memoization + DP 
        # O(n)
        memo = {}
        def dfs(steps):
            if steps in memo:
                return memo[steps]
            if steps <= 1:
                return 1
            memo[steps] = dfs(steps - 1) + dfs(steps - 2)
            return memo[steps]
        return dfs(n)

        