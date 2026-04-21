class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [math.inf] * len(nums)

        dp[0] = 0

        for i in range(1, len(nums)):
            for j in range(i):
                if i - j <= nums[j]:
                    dp[i] = min(dp[i], dp[j] + 1)

        
        return dp[len(nums) - 1]