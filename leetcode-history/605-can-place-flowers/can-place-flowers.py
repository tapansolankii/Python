class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            # Check if current plot is empty
            if flowerbed[i] == 0:
                # Check if left and right spots are empty or out of bounds
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if empty_left and empty_right:
                    # Plant the flower
                    flowerbed[i] = 1
                    count += 1
                    
                    # Optimization: If we've already planted enough, return True early
                    if count >= n:
                        return True
        
        return count >= n