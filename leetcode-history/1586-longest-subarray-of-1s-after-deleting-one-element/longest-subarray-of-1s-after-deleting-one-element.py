class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        zeros = 0
        max_len = 0
        
        for right in range(len(nums)):
            # If we encounter a 0, increment our zero counter
            if nums[right] == 0:
                zeros += 1
            
            # If we have more than one zero, shrink the window from the left
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # The window size is (right - left + 1).
            # But we MUST delete one element, so the 1s count is (right - left).
            max_len = max(max_len, right - left)
            
        return max_len