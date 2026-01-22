import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        n = len(costs)
        head_heap = []
        tail_heap = []
        
        
        left = candidates
        right = max(candidates, n - candidates) - 1
        
     
        for i in range(candidates):
            heapq.heappush(head_heap, costs[i])
        
        
        for i in range(max(candidates, n - candidates), n):
            heapq.heappush(tail_heap, costs[i])
            
        total_cost = 0
        
        for _ in range(k):
   
            val1 = head_heap[0] if head_heap else float('inf')
            val2 = tail_heap[0] if tail_heap else float('inf')
            
            if val1 <= val2:
                total_cost += heapq.heappop(head_heap)
               
                if left <= right:
                    heapq.heappush(head_heap, costs[left])
                    left += 1
            else:
                total_cost += heapq.heappop(tail_heap)
               
                if left <= right:
                    heapq.heappush(tail_heap, costs[right])
                    right -= 1
                    
        return total_cost