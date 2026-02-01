class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if not prices:
            return 0
        
       
        free = 0
        hold = -prices[0]
        
        for i in range(1, len(prices)):
           
            free = max(free, hold + prices[i] - fee)
            
          
            hold = max(hold, free - prices[i])
            
        
        return free