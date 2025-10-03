class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        a, b = 0, len(height) - 1
        while a < b:
            curr_area = 0
            width = b - a
            if height[a] < height[b]:
                curr_area = height[a] * width
                a += 1
            elif height[a] > height[b]:
                curr_area = height[b] * width
                b -= 1
            else:
                curr_area = height[a] * width
                a += 1
            area = max(area, curr_area)
        return area