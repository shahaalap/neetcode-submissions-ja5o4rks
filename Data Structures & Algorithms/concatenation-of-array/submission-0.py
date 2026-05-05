class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [0] * (len(nums) * 2)
        j = len(nums)

        for i,num in enumerate(nums):
            result[i] = num
            result[j] = num
            j += 1

        return result