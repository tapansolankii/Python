from collections import deque
import bisect

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        initial_zeros = s.count('0')
        if initial_zeros == 0: return 0
        
 
        unvisited_even = sorted([z for z in range(0, n + 1, 2) if z != initial_zeros])
        unvisited_odd = sorted([z for z in range(1, n + 1, 2) if z != initial_zeros])
        
        queue = deque([(initial_zeros, 0)])
        
        while queue:
            z, steps = queue.popleft()
            
            low = abs(z - k)
            high = n - abs((n - z) - k)
            
         
            target_list = unvisited_even if low % 2 == 0 else unvisited_odd
            
   
            left_idx = bisect.bisect_left(target_list, low)
            right_idx = bisect.bisect_right(target_list, high)
            
      
            to_add = target_list[left_idx:right_idx]
            
            for new_z in to_add:
                if new_z == 0: return steps + 1
                queue.append((new_z, steps + 1))
            
          
            del target_list[left_idx:right_idx]
                
        return -1