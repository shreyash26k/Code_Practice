from collections import defaultdict


class Solution(object):

  def maximumLengthSubstring(self, s):
    freq = defaultdict(int)
    l = 0
    max_len = 0

    for r in range(len(s)):
      freq[s[r]] += 1

      while freq[s[r]] > 2:
        freq[s[l]] -= 1 
        l += 1

      max_len = max(max_len, r - l + 1)

    return max_len