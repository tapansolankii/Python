from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap)>k:
                heapq.heappop(minHeap)
        return minHeap[0]


sol = Solution()
nums = [3,2,1,5,6,4]
k = 2
result = sol.findKthLargest(nums, k)
print(result)


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\16_minHeap_kth_element.py
# 5
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 