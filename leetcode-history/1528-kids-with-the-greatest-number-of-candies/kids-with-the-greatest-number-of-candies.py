class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        # Step 1: Find the maximum value in the original list
        max_candies = max(candies)
        
        # Step 2: Create the result list by checking each kid
        result = []
        for candy in candies:
            # If current kid + extra >= the original max, it's True
            if candy + extraCandies >= max_candies:
                result.append(True)
            else:
                result.append(False)
        
        return result