class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        lb=0
        lr=0
        maxb=0
        for i in s:
            if i == '(':
                lb+=1
            elif i == ')':
                lr+=1
            maxb=max(maxb,lb-lr)
        return maxb