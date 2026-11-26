class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # If k is at least n // 2, we can capture every upward move
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        buy = [float("-inf")] * (k + 1)
        sell = [0] * (k + 1)

        for price in prices:
            for t in range(1, k + 1):
                buy[t] = max(buy[t], sell[t - 1] - price)
                sell[t] = max(sell[t], buy[t] + price)

        return sell[k]