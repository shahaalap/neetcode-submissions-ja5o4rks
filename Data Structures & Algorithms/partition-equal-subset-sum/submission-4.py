class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 > 0:
            return False

        half = total // 2
        n = len(nums) + 1

        dp = [[False] * (half + 1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        for i in range(1, n):
            for j in range(1, half + 1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                elif dp[i-1][j] or dp[i-1][j - nums[i-1]]:
                    dp[i][j] = True
                
                if j == half and dp[i][j]:
                    return True

        return False

            