class Solution(object):

  def uniformArray(self, nums1):
    all_even = all(x % 2 == 0 for x in nums1)
    min_is_odd = min(nums1) % 2 != 0

    return all_even or min_is_odd
    

