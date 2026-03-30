class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, n = 0, len(prices)

        if n < 2:
            return profit

        i , j = 0, 1
        while j < n:
            profit = max(profit, prices[j] - prices[i])

            if prices[i] > prices[j]:
                i = j

            j = j + 1

        return profit
