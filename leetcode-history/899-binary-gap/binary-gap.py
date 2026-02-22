class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """

        last_pos = None
        max_gap = 0
        
        for i in range(31):
          
            if (n >> i) & 1:
                if last_pos is not None:
     
                    max_gap = max(max_gap, i - last_pos)
     
                last_pos = i
                
        return max_gap