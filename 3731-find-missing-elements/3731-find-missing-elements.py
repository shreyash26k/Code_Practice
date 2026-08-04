class Solution(object):

  def findMissingElements(self, nums):
    """:type nums: List[int]

    :rtype: List[int]
    """
    num_set = set(nums)
    start = min(nums)
    end = max(nums)

    output = []
    for i in range(start, end + 1):
      if i not in num_set:
        output.append(i)

    return output
        