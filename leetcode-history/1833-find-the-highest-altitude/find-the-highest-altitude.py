class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        current_altitude = 0
        max_altitude = 0
        
        for g in gain:
            # Update current altitude by adding the gain/loss
            current_altitude += g
            
            # Check if this new altitude is the highest we've seen
            if current_altitude > max_altitude:
                max_altitude = current_altitude
                
        return max_altitude