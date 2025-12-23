import fractions

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Step 1: Verification check
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: Use fractions.gcd for Python 2 compatibility
        # Or you can use a manual while loop
        gcd_len = self.get_gcd(len(str1), len(str2))
        
        return str1[:gcd_len]

    def get_gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a