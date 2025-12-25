class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0
        read = 0
        
        while read < len(chars):
            char = chars[read]
            count = 0
            
            # Find the length of the current group of identical characters
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1
            
            # 1. Write the character itself
            chars[write] = char
            write += 1
            
            # 2. Write the count if it's greater than 1
            if count > 1:
                # Convert count to string to handle multi-digit numbers (e.g., 12 -> '1', '2')
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        # The 'write' pointer now represents the new length of the compressed array
        return write