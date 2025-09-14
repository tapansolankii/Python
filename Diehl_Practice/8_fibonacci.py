# Question 3: Fibonacci Sequence
# Write a function to generate the first 
# 𝑛
# n numbers of the Fibonacci sequence.

def fibonacci(n):
    # Your code here
    # pass
    if n==0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0,1]
    sequence = [0,1]
    for i in range(2,n):
        count = sequence[i-1]+sequence[i-2]
        sequence.append(count)
    return sequence

# Example:
n = 7
print(fibonacci(n))
# Output: [0, 1, 1, 2, 3, 5, 8]

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\8_fibonacci.py
# [0, 1, 1, 2, 3, 5, 8]
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 