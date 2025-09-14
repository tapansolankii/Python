# Question 5: Maximum Subarray
# Given an integer array nums, find the contiguous 
# subarray (containing at least one number) which 
# has the largest sum, and return its sum.




# My approach - gave output as 5 instead of 6.
# def max_subarray(nums):
#     # Your code here
#     # pass
#     count = 0
#     result = -float('inf')
#     start, end = 0, len(nums)-1
#     for i in range(len(nums)):
#         count+=nums[i]
#     while start<=end:
#         if nums[start]<=nums[end]:
#             count-=nums[start]
#             start+=1
#             result=max(result, count)
#         else:
#             count-=nums[end]
#             end-=1
#             result=max(result, count)
#     return result

# ChatGPT using 2 pointers.
def max_subarray(nums):
    left, right = 0, 0
    current_sum = 0
    max_sum = -float('inf')

    while right < len(nums):
        # Expand the window by including nums[right]
        current_sum += nums[right]
        max_sum = max(max_sum, current_sum)

        # Shrink the window if the current sum becomes negative
        while current_sum < 0 and left <= right:
            current_sum -= nums[left]
            left += 1

        # Move the right pointer to expand the window
        right += 1

    return max_sum


def max_subarray_2(nums):
    # Initialize the current sum and max sum
    current_sum = 0
    max_sum = -float('inf')
    
    for num in nums:
        # If current sum becomes negative, reset it to 0
        current_sum = max(num, current_sum + num)
        # Update the maximum sum found so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum




# Example:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray(nums))
print(max_subarray_2(nums))
# Output: 6 (subarray [4, -1, 2, 1] has the largest sum)

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\17_highestSum.py
# 6
# 6
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 