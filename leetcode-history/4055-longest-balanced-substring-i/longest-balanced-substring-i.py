class Solution(object):
    def longestBalanced(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 1  

        for i in range(n):
            freq = [0] * 26
            for j in range(i, n):
                freq[ord(s[j]) - 97] += 1

                mn = 10**9
                mx = 0
                has = False

                for c in freq:
                    if c:
                        has = True
                        if c < mn: mn = c
                        if c > mx: mx = c

                if has and mn == mx:
                    ans = max(ans, j - i + 1)

        return ans