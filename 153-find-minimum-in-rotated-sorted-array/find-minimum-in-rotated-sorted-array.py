class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Need to use a modified Binary Search
        l, r = 0, len(nums) - 1
        # Assume left-most element is smallest
        res = nums[l]
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l + r)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res