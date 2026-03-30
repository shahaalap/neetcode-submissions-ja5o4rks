class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numset = {}

        for i, num in enumerate(nums):
            j = target - num
            if j in numset:
                return [numset[j], i]

            numset[num] = i                
