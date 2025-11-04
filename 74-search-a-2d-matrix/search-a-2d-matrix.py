class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Two Binary searches
        # First to check what row the target might be in
        # Second to check the row if target is present
        # O(logm + logn) = O(logm*n)
        r, c = len(matrix), len(matrix[0])
        top, bot = 0, r - 1

        # O(logm)
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        left, right = 0, c - 1

        # O(logn)
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False
        