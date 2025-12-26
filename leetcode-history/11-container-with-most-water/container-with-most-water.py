class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate the distance between lines
            width = right - left
            
            # The water level is limited by the shorter of the two lines
            h = min(height[left], height[right])
            
            # Update the maximum area found so far
            max_water = max(max_water, width * h)
            
            # Move the pointer pointing to the shorter line
            # This is the "greedy" step: the only way to find a larger area
            # is to find a taller line to replace the current limiting factor.
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water