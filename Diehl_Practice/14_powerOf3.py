# Question 3: Power of Three
# Write a function to check if a number is a power of 
# three. Return True if it is, otherwise False.

def is_power_of_three(n):
    # Your code here
    # pass
    if n<=0:
        return False
    num = 3
    while(num<=n):
        num*=3
        if num==n:
            return True
    return False
    
def is_power_of_three_2(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1


n = 27
print(is_power_of_three(n))  
print(is_power_of_three_2(n))  
# Output: True (because 27 = 3^3)

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\14_powerOf3.py
# True
# True
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 