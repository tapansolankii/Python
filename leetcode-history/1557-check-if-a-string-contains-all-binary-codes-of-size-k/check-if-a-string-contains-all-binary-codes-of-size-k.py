class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
      
        required_count = 1 << k
        seen_codes = set()
        
        
        for i in range(len(s) - k + 1):
            substring = s[i : i + k]
            seen_codes.add(substring)
            
           
            if len(seen_codes) == required_count:
                return True
                
        return False