"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        result  = 0
        if len(intervals) == 0:
            return result

        intervals.sort(key = lambda x : x.start)
        minheap = []

        for i in range(len(intervals)):
            start, end = intervals[i].start, intervals[i].end
            while len(minheap) and minheap[0][0] <= start:
                heapq.heappop(minheap)
            
            heapq.heappush(minheap, (end, start))
            result = max(result, len(minheap))
        
        
        return result

