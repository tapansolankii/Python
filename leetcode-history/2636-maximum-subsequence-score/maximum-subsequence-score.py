import heapq

class Solution(object):
    def maxScore(self, nums1, nums2, k):
       
        pairs = sorted(zip(nums1, nums2), key=lambda x: x[1], reverse=True)
        
        min_heap = []
        current_sum = 0
        max_score = 0
        
        for n1, n2 in pairs:
            
            heapq.heappush(min_heap, n1)
            current_sum += n1
            
            
            if len(min_heap) > k:
                current_sum -= heapq.heappop(min_heap)
            
            if len(min_heap) == k:
                max_score = max(max_score, current_sum * n2)
                
        return max_score