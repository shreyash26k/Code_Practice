class Solution(object):
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0

        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in counts:
            if counts[ch] < k:                      
                return max(self.longestSubstring(part, k)
                           for part in s.split(ch))

        return len(s)                              