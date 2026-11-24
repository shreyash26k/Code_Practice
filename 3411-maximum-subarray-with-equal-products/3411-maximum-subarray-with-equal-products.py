class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return a * b // gcd(a, b)

        best = 0
        n = len(nums)
        for i in range(n):              
            p = 1                       
            g = 0                     
            l = 1                       
            for j in range(i, n):       
                p *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                if p == g * l:
                    best = max(best, j - i + 1)
        return best