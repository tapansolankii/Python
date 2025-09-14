# Question 1: Two Sum
# Given an array of integers nums and an integer target, 
# return the indices of the two numbers such that they 
# add up to the target.

def two_sum(nums, target):
    # Your code here
    # pass
    num_map = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num]=i

# Example:
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
# Output: [0, 1] (because nums[0] + nums[1] = 9)
