class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Count vowels in the first window
        current_vowels = 0
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
        
        max_vowels = current_vowels
        
        # If we already found k vowels, we can't do better
        if max_vowels == k:
            return k
            
        # Slide the window
        for i in range(k, len(s)):
            # Add new character
            if s[i] in vowels:
                current_vowels += 1
            # Remove old character
            if s[i - k] in vowels:
                current_vowels -= 1
            
            # Update max and early exit if k is reached
            if current_vowels > max_vowels:
                max_vowels = current_vowels
                if max_vowels == k:
                    return k
                    
        return max_vowels