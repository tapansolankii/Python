class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        # Step 1: Initialize the window sum with the first k elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Step 2: Slide the window from index k to the end of the array
        for i in range(k, len(nums)):
            # Add the next element and subtract the first element of the previous window
            current_sum += nums[i] - nums[i - k]
            
            # Update max_sum if the new window sum is larger
            if current_sum > max_sum:
                max_sum = current_sum
                
        # Step 3: Return the average as a float
        return float(max_sum) / k