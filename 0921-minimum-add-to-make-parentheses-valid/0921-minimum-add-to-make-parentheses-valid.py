class Solution(object):
    def minAddToMakeValid(self, s):
        o=0
        add=0
        for i in s:
            if i == "(":
                o+=1
            else:
                if o>0:
                    o-=1
                else:
                    add+=1
        return add+o
        