class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        groups = []
        if not s:
            return 0
        
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count += 1
            else:
                groups.append(count)
                count = 1
        groups.append(count) 
        
        
        ans = 0
        for i in range(1, len(groups)):
            ans += min(groups[i], groups[i-1])
            
        return ans