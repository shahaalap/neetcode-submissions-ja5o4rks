class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result, n = 0, len(prices)

        if n < 2:
            return result

        buy, sell = 0, 1

        for sell in range(n):
            result = max(result, prices[sell] - prices[buy])

            if prices[sell] < prices[buy]:
                buy = sell

        return result