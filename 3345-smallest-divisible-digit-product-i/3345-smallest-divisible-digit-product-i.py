class Solution(object):
    def smallestNumber(self, n, t):
        i = n
        while True:
            prod = 1
            for digit in str(i):
                prod *= int(digit)
            
            if prod % t == 0:
                return i
            
            i += 1