class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        # Backtracking to find all possible subsets
        # O(n x 2^n)
        def backtrack(start, subset):
            result.append(subset[:])
            for i in range(start, len(nums)):
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()
        backtrack(0, [])
        return result




        