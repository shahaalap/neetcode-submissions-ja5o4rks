class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningsum = nums[0]
        result = runningsum

        for i in range(1, len(nums)):
            if runningsum < 0:
                runningsum = 0

            runningsum += nums[i]
            result = max(result, runningsum)

        return result