class Solution(object):
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            take_sum = 0
            best_diff = float('-inf')
            
            for k in range(1, 4):
                if i + k - 1 < n:
                    take_sum += stoneValue[i + k - 1]
                    best_diff = max(best_diff, take_sum - dp[i + k])
            
            dp[i] = best_diff
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"