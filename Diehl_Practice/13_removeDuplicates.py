# Question 2: Remove Duplicates from Sorted Array
# Given a sorted array, remove duplicates in-place 
# such that each element appears only once. Return the 
# new length of the array.

# but this doesn't remove in-place.
# it uses an extra dataset.
def remove_duplicates(nums):
    # Your code here
    # pass
    mySet = set(nums)
    return list(mySet)


def remove_duplicates_2(nums):
    if not nums:
        return None
    unique_position = 0
    for i in range(1, len(nums)):
        if nums[i]!=nums[unique_position]:
            unique_position+=1
            nums[unique_position]=nums[i]
    return unique_position+1


# Example:
nums = [1, 1, 2, 2, 3]
nums_copy = nums[:]
nums_copy_2 = nums_copy[:]
print(remove_duplicates(nums))

print(remove_duplicates_2(nums_copy))

length = remove_duplicates_2(nums_copy_2)
print(f'The length is {length}. The array is {nums_copy_2[:length]}')



# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\13_removeDuplicates.py
# [1, 2, 3]
# 3
# The length is 3. The array is [1, 2, 3]
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice>