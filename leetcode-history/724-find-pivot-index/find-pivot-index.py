class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_sum = sum(nums)
        left_sum = 0
        
        for i, val in enumerate(nums):
            # The right sum is: total_sum - left_sum - current_element
            # We check if left_sum == right_sum
            if left_sum == (total_sum - left_sum - val):
                return i
            
            # Update left_sum for the next index
            left_sum += val
            
        return -1