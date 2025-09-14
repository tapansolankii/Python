
# Question 2: Find All Duplicates in a List
# Write a function to find all duplicate numbers in a list. 
# The result should be a list of duplicates.

def find_duplicates(nums):
    # Your code here
    # pass
    frequency = {}
    duplicates = []
    for num in nums:
        frequency[num] = frequency.get(num,0) +1
    for num, count in frequency.items():
        if count>1:
            duplicates.append(num)
    return duplicates

# Example:
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(nums))
# Output: [2, 3]

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\7_findDuplicates.py
# [3, 2]
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 


# or
# def find_duplicates(nums):
#     seen = set()
#     duplicates = set()

#     for num in nums:
#         if num in seen:
#             duplicates.add(num)
#         else:
#             seen.add(num)

#     return list(duplicates)
