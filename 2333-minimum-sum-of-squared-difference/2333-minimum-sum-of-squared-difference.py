class Solution(object):

  def minSumSquareDiff(self, nums1, nums2, k1, k2):
    n = len(nums1)
    diffs = [abs(nums1[i] - nums2[i]) for i in range(n)]
    total_diff = sum(diffs)
    k_total = k1 + k2
    
    if total_diff <= k_total:
      return 0
    max_diff = max(diffs)
    count = [0] * (max_diff + 1)
    for d in diffs:
      count[d] += 1
    for d in range(max_diff, 0, -1):
      if count[d] > 0:
        reduction = min(k_total, count[d])
        count[d] -= reduction
        count[d - 1] += reduction
        k_total -= reduction

        if k_total == 0:
          break
    result = 0
    for d in range(max_diff + 1):
      if count[d] > 0:
        result += count[d] * (d**2)

    return result
        