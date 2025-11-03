class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        l, r = 0, len(height)-1
        while l < r:
            width = (r+1) - (l+1)
            if height[l] > height[r]:
                area = max(area, height[r]*width)
                r -= 1
            elif height[l] < height[r]:
                area = max(area, height[l]*width)
                l += 1
            else:
                area = max(area, height[l]*width)
                l += 1
        return area