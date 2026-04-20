class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i, j = 0, len(intervals) - 1

        while i <= j:
            mid = i + ((j - i) //2)
            if intervals[mid][0] <= newInterval[0]:
                i = mid + 1
            else:
                j = mid - 1

        intervals.insert(i, newInterval)

        result = []
        if len(intervals) > 0:
            result.append(intervals[0])

        n = len(intervals)
        i = 1
        while i < n:
            if result[-1][0] <= intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(intervals[i][1], result[-1][1])
            else:
                result.append(intervals[i])

            i += 1

        return result