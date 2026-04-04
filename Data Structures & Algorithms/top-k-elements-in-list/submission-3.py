class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        bucket = [[] for _ in range(len(nums) + 1)]
        counts =Counter(nums)
        result = []

        for num, count in counts.items():
            bucket[count].append(num)

        for i in range(len(nums), -1, - 1):
            while bucket[i] and k > 0:
                result.append(bucket[i].pop())
                k -= 1
            
            if k == 0:
                break

        return result
