class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        cur_sum=0
        for i in range(k):
            cur_sum+=nums[i]
        max_avg=float(cur_sum)/k

        for i in range(k,len(nums)):
            cur_sum+=nums[i]
            cur_sum-=nums[i-k]
            avg=float(cur_sum)/k
            max_avg=max(max_avg,avg)
    
        return max_avg
        