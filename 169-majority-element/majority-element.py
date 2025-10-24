class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Prefer the Moore Voting Algorithm
        # Assumes that 1st number is the majority element
        # Increments count if we encounter the same element, else decrements it
        # If count reaches 0, that means another element is majority
        # Return candidate number with count > 0

        count = 0
        candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
        