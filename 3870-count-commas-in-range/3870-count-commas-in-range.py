class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum=0
        for i in range(1,n+1):
            if i <= 999:
                sum+=0
            else:
                sum+=1
        return sum

        