class Solution(object):

  def longestPalindrome(self, s):
    if not s:
      return ""

    start, max_len = 0, 0

    def expand(left, right):
      while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
      return right - left - 1

    for i in range(len(s)):
      len1 = expand(i, i)
      len2 = expand(i, i + 1)

      current_len = max(len1, len2)
      if current_len > max_len:
        max_len = current_len
        start = i - (current_len - 1) // 2

    return s[start : start + max_len]
        