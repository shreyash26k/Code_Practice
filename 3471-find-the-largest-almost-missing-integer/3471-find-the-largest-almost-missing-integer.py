from collections import Counter

class Solution(object):
    def largestInteger(self, nums, k):
        n = len(nums)
        counts = Counter(nums)
        
        if k == 1:
            candidates = [x for x in nums if counts[x] == 1]
            return max(candidates) if candidates else -1
        
        if k == n:
            return max(nums)
        
        ans = -1
        if counts[nums[0]] == 1:
            ans = max(ans, nums[0])
        if counts[nums[-1]] == 1:
            ans = max(ans, nums[-1])
            
        return ans