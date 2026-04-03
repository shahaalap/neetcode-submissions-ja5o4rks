class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap, result = [], []

        for x1, y1 in points:
            distance = math.sqrt((x1 - 0) ** 2 + (y1 - 0) ** 2)
            heapq.heappush(minheap, (-distance, [x1, y1]))
            if len(minheap) > k:
                heapq.heappop(minheap)

        while len(minheap) > 0:
            result.append(heapq.heappop(minheap)[1])

        return result