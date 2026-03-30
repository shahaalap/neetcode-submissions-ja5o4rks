class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        keys = {}

        for i, num in enumerate(nums):
            j = target - num

            if j in keys:
                return [keys[j], i]
            else:
                keys[num] = i

        