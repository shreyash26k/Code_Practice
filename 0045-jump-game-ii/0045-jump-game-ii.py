class Solution(object):
    def jump(self, nums):
        far = 0
        end = 0
        jumps = 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == end:
                jumps += 1
                end = far
        return jumps