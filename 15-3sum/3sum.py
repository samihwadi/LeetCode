class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            j, k = i + 1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                if total > 0:
                    k -= 1
                if total < 0:
                    j += 1
        return result
                
                    