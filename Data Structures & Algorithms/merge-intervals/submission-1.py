class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            cur = intervals[i]
            prev = result[-1]

            if cur[0] <= prev[1]:
                prev[1] = max(prev[1], cur[1])
            else:
                result.append(cur)

        return result

            




