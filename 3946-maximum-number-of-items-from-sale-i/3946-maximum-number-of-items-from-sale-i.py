class Solution:
    def maximumSaleItems(self, items, budget):
        n = len(items)

        c = [0] * n
        for i in range(n):
            for j in range(n):
                if j != i and items[j][0] % items[i][0] == 0:
                    c[i] += 1

        dp = [0] * (budget + 1)
        for i in range(n):
            price = items[i][1]
            value = 1 + c[i]
            for b in range(budget, price - 1, -1):  
                dp[b] = max(dp[b], dp[b - price] + value)
        min_price = min(p for _, p in items)
        return max(dp[b] + (budget - b) // min_price for b in range(budget + 1))
