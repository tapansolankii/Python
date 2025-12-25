class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Initialize first and second to the largest possible values
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            if n <= first:
                # Update the smallest value found so far
                first = n
            elif n <= second:
                # Update the second smallest value (but greater than first)
                second = n
            else:
                # If we find a number greater than 'second', 
                # we've found our triplet (first < second < n)
                return True
                
        return False