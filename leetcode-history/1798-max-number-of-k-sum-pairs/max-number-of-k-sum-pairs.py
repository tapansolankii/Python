class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Step 1: Sort the array to use two pointers
        nums.sort()
        
        left = 0
        right = len(nums) - 1
        count = 0
        
        # Step 2: Use pointers to find pairs that sum to k
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == k:
                # Pair found: increment count and move both pointers
                count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                # Sum too small: move left pointer to increase sum
                left += 1
            else:
                # Sum too large: move right pointer to decrease sum
                right -= 1
                
        return count