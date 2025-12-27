class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        max_length = 0
        zero_count = 0
        
        # 'right' expands the window
        for right in range(len(nums)):
            # If we find a zero, we "use" one of our k flips
            if nums[right] == 0:
                zero_count += 1
            
            # If we've used more than k flips, shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Calculate the current window size and update max_length
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)
            
        return max_length