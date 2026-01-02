class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        
        
        occurrence_values = counts.values()
        
        
        return len(occurrence_values) == len(set(occurrence_values))