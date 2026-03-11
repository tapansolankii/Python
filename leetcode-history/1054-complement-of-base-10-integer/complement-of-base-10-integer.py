class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Edge case: if n is 0, the complement is 1
        if n == 0:
            return 1
        
        num_bits = len(bin(n)) - 2
        
        
        mask = (1 << num_bits) - 1
        

        return n ^ mask