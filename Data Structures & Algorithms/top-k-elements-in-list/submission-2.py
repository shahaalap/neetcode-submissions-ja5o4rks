class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        topkitems = []

        for num, count in counts.items():
            heapq.heappush(topkitems, (count, num))
            if len(topkitems) > k:
                heapq.heappop(topkitems)
            
        return [i[1] for i in topkitems]