class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_len = 0
        

        for i in range(n):
            distinct_evens = set()
            distinct_odds = set()
            

            for j in range(i, n):
                val = nums[j]
                

                if val % 2 == 0:
                    distinct_evens.add(val)
                else:
                    distinct_odds.add(val)
                
       
                if len(distinct_evens) == len(distinct_odds):
                    current_len = j - i + 1
                    if current_len > max_len:
                        max_len = current_len
                        
        return max_len