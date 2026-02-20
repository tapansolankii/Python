class Solution(object):
    def makeLargestSpecial(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = 0
        i = 0
        res = []
        
        for j, char in enumerate(s):
           
            count += 1 if char == '1' else -1
            
          
            if count == 0:
               
                inner_content = self.makeLargestSpecial(s[i + 1:j])
                res.append('1' + inner_content + '0')
                
              
                i = j + 1
        
       
        return "".join(sorted(res, reverse=True))
