class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.size = k
        self.minheap = nums
        
        heapq.heapify(nums)
        while len(self.minheap) > self.size:
            heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        
        heapq.heappush(self.minheap, val)

        if len(self.minheap) > self.size:
            heapq.heappop(self.minheap)

        return self.minheap[0]
        
