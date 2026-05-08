from collections import deque, defaultdict
import math
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 1:
            return 0
            
        max_val = max(nums)
        
        
        is_prime = [True] * (max_val + 1)
        if max_val >= 0: is_prime[0] = False
        if max_val >= 1: is_prime[1] = False
        
        for p in range(2, int(math.isqrt(max_val)) + 1):
            if is_prime[p]:
                for i in range(p * p, max_val + 1, p):
                    is_prime[i] = False
                    
       
        value_to_indices = defaultdict(list)
        for i, val in enumerate(nums):
            value_to_indices[val].append(i)
            
        
        queue = deque([(0, 0)]) 
        visited_indices = {0}
        used_primes = set()
        
        while queue:
            curr_idx, steps = queue.popleft()
            
            
            if curr_idx == n - 1:
                return steps
                
            
            for next_idx in (curr_idx - 1, curr_idx + 1):
                if 0 <= next_idx < n and next_idx not in visited_indices:
                    visited_indices.add(next_idx)
                    queue.append((next_idx, steps + 1))
                    
            
            val = nums[curr_idx]
            if is_prime[val] and val not in used_primes:
                used_primes.add(val)
                
                
                for multiple in range(val, max_val + 1, val):
                    if multiple in value_to_indices:
                        for target_idx in value_to_indices[multiple]:
                            if target_idx not in visited_indices:
                                visited_indices.add(target_idx)
                                queue.append((target_idx, steps + 1))
                                
                        
                        value_to_indices[multiple].clear()
                        
        return -1 