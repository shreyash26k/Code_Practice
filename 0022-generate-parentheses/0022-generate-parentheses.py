class Solution(object):
    def generateParenthesis(self, n):
        out = []
        
        def build(s, o, c):
            if len(s) == 2 * n:
                out.append(s)
                return
            if o < n:
                build(s + "(", o + 1, c)
            if c < o:
                build(s + ")", o, c + 1)

        build("", 0, 0)
        return out