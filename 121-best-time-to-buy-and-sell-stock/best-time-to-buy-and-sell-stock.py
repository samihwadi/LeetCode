class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min_num = prices[0]
        max_diff = 0
        for num in prices[1:]:
            max_diff = max(num - min_num, max_diff)
            min_num = min(num, min_num)
        return max_diff
            

        