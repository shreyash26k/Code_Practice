class Solution(object):

  def firstStableIndex(self, nums, k):
    max_val = float("-inf")

    for i in range(len(nums)):
      max_val = max(max_val, nums[i])
      min_val = min(nums[i:]) 
      if max_val - min_val <= k:
        return i

    return -1
            