class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            # For each existing subset, add a new subset including num
            result += [curr + [num] for curr in result]
        return result




        