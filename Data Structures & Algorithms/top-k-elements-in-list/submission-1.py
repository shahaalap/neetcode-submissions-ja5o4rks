class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        freqmap = {}

        for i in range(1, len(nums) + 1):
            freqmap[i] = []

        for num, count in count.items():
            freqmap[count].append(num)

        result = []
       
        for i in range(len(nums), 0, -1):
            while k > 0 and freqmap[i]:
                result.append(freqmap[i].pop())
                k -= 1
            
        return result
        