class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []

        heaplist = []
        for num, count in count.items():
            heapq.heappush(heaplist,(-count, num))

        
        while k:
            curItem = heapq.heappop(heaplist)
            result.append(curItem[1])
            k -= 1

        return result

