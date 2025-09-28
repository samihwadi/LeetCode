class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Array is sorted but rotated between 1 and n
        # Modified Binary Search to achieve O(logn)
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

        