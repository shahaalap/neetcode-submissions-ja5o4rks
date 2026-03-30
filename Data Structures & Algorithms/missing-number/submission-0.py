class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        ideal = sum(range(len(nums) + 1))
        actual = sum(nums)

        return ideal - actual
        