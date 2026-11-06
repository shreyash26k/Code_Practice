class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}   # Maps char -> most recent index
        start = 0        # Left edge of current sliding window
        max_len = 0
        
        for end, ch in enumerate(s):
            # If the character is inside our current window, move window start past it
            if ch in last_seen and last_seen[ch] >= start:
                start = last_seen[ch] + 1
            
            # These must be OUTSIDE the `if` block so they execute for every character:
            last_seen[ch] = end
            max_len = max(max_len, end - start + 1)
            
        return max_len
        