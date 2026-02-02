from sortedcontainers import SortedList

class Solution(object):
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        m = k - 1 
        
 
        small = SortedList()
      
        large = SortedList()
        
        current_small_sum = 0

        for i in range(1, dist + 2):
            small.add(nums[i])
            current_small_sum += nums[i]
            

        while len(small) > m:
            val = small.pop() 
            current_small_sum -= val
            large.add(val)
            
        ans = current_small_sum
        
        
        for i in range(dist + 2, n):
           
            out_val = nums[i - dist - 1]
            if out_val in small:
                small.remove(out_val)
                current_small_sum -= out_val
            else:
                large.remove(out_val)
            
          
            large.add(nums[i])
            
           
            if len(small) < m:
                move_val = large.pop(0)
                small.add(move_val)
                current_small_sum += move_val
            
         
            if small and large and small[-1] > large[0]:
                s_val = small.pop()
                l_val = large.pop(0)
                current_small_sum -= s_val
                current_small_sum += l_val
                small.add(l_val)
                large.add(s_val)
                
            ans = min(ans, current_small_sum)
            
        return ans + nums[0]