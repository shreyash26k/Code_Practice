class Solution(object):

  def maxArea(self, height):
    """:type height: List[int]

    :rtype: int
    """
    left, right = 0, len(height) - 1
    maxw = 0

    while left < right:
      h = min(height[left], height[right])
      w = right - left
      maxw = max(maxw, h * w)

      if height[left] < height[right]:
        left += 1
      else:
        right -= 1

    return maxw