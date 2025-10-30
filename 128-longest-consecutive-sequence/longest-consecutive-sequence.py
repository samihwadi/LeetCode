class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sorting would be easier but O(nlogn) -> X
        # Hash Set to remove duplicates 
        # Find number which is start of a sequence, i.e, hashset does not contain nums[i] - 1
        # Track length of sequence
        my_nums = set(nums)
        longest = 0
        for n in my_nums:
            # Find start of sequence
            if n - 1 not in my_nums:
                length = 0
                while n + length in my_nums:
                    length += 1
                longest = max(length, longest)
        return longest
