# Question 1: Find the Missing Number
# You are given a list containing 
# 𝑛
# n unique integers from 1 to 
# 𝑛
# +
# 1
# n+1. One number is missing. Write a function to find the missing number.

def find_missing_number(arr):
    # Your code here
    n = len(arr)+1
    count = actual = 0
    for i in range (1,n+1):
        count+=i
    for i in range(n-1):
        actual+=arr[i]
    return count - actual
    # pass

# Example:
arr = [1, 2, 4, 6, 3, 7, 8]
print(find_missing_number(arr))  # Output: 5

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\1_missingNumber.py
# 5
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 
