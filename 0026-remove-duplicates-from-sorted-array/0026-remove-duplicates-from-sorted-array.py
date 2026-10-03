class Solution(object):
    def removeDuplicates(self, nums):
        seen=[]
        k=0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.append(nums[i])
                nums[k] = nums[i]
                k+=1
        return k

        
        