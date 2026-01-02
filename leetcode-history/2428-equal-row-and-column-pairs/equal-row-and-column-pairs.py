from collections import Counter

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        
        row_counts = Counter(tuple(row) for row in grid)
        
        count = 0
        
        
        for j in range(n):
            # Construct the column tuple
            col = tuple(grid[i][j] for i in range(n))
            
            
            count += row_counts[col]
            
        return count