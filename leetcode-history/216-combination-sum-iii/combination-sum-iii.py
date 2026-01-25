class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        
        def backtrack(remain, comb, start):
           
            if len(comb) == k:
                if remain == 0:
                    results.append(list(comb))
                return
            
            
            if remain < 0:
                return

           
            for i in range(start, 10):
                comb.append(i)
                
                backtrack(remain - i, comb, i + 1)
                
                comb.pop()

        backtrack(n, [], 1)
        return results