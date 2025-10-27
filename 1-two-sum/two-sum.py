class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Every input has at least one pair that satisfies
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i
        