class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
       
        row = [1] * n
        
        
        for i in range(m - 1):
            
            for j in range(1, n):
                
                row[j] = row[j] + row[j - 1]
                
        return row[-1]