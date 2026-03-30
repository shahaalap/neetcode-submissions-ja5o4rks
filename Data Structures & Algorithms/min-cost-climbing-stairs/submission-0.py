class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1] * n
        cache[0], cache[1] = cost[0], cost[1]

        def dfs(i):
            if i < 0:
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = cost[i] + min(dfs(i - 1), dfs(i - 2))
            return cache[i]

        dfs(n - 1)

        return min(cache[n-1], cache[n-2])