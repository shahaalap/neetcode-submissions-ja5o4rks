class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if n == 0:
            return 0
        elif n == 1:
            return stones[0]

        stonesheap = []
        for stone in stones:
            heapq.heappush(stonesheap, -stone)

        while len(stonesheap) > 1:
            max1 = -heapq.heappop(stonesheap)
            max2 = -heapq.heappop(stonesheap)

            newstone = abs(max1 - max2)

            heapq.heappush(stonesheap, -newstone)

        return -heapq.heappop(stonesheap)



