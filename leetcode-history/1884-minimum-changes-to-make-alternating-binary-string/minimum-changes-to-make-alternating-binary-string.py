class Solution:
    def minOperations(self, s: str) -> int:
        mism0 = 0  
        mism1 = 0 

        for i, ch in enumerate(s):
            expected0 = '0' if i % 2 == 0 else '1'
            expected1 = '1' if i % 2 == 0 else '0'
            if ch != expected0:
                mism0 += 1
            if ch != expected1:
                mism1 += 1

        return min(mism0, mism1)