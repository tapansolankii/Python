class Solution(object):
    def maxSumTrionic(self, nums):
        n = len(nums)
        if n < 4: return 0
        
        # 1. Max sum of strictly increasing subarray ending at i (length >= 2)
        max_inc_end = [-float('inf')] * n
        curr_sum = -float('inf')
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # Either extend the streak or start a new pair (nums[i-1], nums[i])
                curr_sum = max(nums[i-1] + nums[i], curr_sum + nums[i])
                max_inc_end[i] = curr_sum
            else:
                curr_sum = -float('inf')

        # 2. Max sum of strictly increasing subarray starting at i (length >= 2)
        max_inc_start = [-float('inf')] * n
        curr_sum = -float('inf')
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i+1]:
                curr_sum = max(nums[i] + nums[i+1], curr_sum + nums[i])
                max_inc_start[i] = curr_sum
            else:
                curr_sum = -float('inf')

        # 3. Precompute prefix sums for middle calculation
        prefix_sums = [0] * (n + 1)
        for i in range(n):
            prefix_sums[i+1] = prefix_sums[i] + nums[i]

        ans = -float('inf')
        
        # 4. Use a more robust approach to find decreasing middle segments
        # A trionic subarray is (Up) -> (Down) -> (Up)
        # We need p (peak) and q (valley) such that nums[p...q] is strictly decreasing.
        
        # Find all local strictly decreasing sequences
        i = 0
        while i < n - 1:
            if nums[i] > nums[i+1]:
                start = i
                while i + 1 < n and nums[i] > nums[i+1]:
                    i += 1
                end = i
                
                # Now we have a decreasing range [start, end]
                # peak p can be in [start, end-1], valley q can be in [p+1, end]
                best_p_val = -float('inf')
                for k in range(start, end + 1):
                    # Try k as valley q
                    if k > start and max_inc_start[k] != -float('inf') and best_p_val != -float('inf'):
                        # Total = (max_inc_end[p] - prefix_sums[p+1]) + prefix_sums[k] + max_inc_start[k]
                        ans = max(ans, best_p_val + prefix_sums[k] + max_inc_start[k])
                    
                    # Try k as peak p
                    if k < end and max_inc_end[k] != -float('inf'):
                        best_p_val = max(best_p_val, max_inc_end[k] - prefix_sums[k+1])
            else:
                i += 1

        return int(ans)