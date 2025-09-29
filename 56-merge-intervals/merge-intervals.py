class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= result[-1][1]:
                # Merge them by updating the end of the last interval
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                # No overlap, just append
                result.append(intervals[i])
        return result


