class Solution(object):
    def minSwaps(self, nums):
        def get_digit_sum(n):
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s

        n = len(nums)
        
        indexed_nums = []
        for i, val in enumerate(nums):
            indexed_nums.append((get_digit_sum(val), val, i))
        sorted_nums = sorted(indexed_nums, key=lambda x: (x[0], x[1]))
        
        target_indices = {}
        for target_idx, item in enumerate(sorted_nums):
            orig_idx = item[2]
            target_indices[orig_idx] = target_idx
            
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if not visited[i] and target_indices[i] != i:
                cycle_size = 0
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    curr = target_indices[curr]
                    cycle_size += 1
            
                if cycle_size > 1:
                    swaps += (cycle_size - 1)
                    
        return swaps