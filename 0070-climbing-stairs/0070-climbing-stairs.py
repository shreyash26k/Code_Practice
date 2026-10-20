class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        # Base cases: ways to reach step 1 and step 2
        prev2 = 1  # ways for n = 1
        prev1 = 2  # ways for n = 2
        
        current = 0
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
            
        return current