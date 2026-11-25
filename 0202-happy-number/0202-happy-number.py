class Solution(object):
    def isHappy(self, n):
        def next_num(m):
            total = 0
            while m > 0:
                digit = m % 10       
                total += digit * digit
                m //= 10             
            return total

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next_num(n)
        return n == 1
            