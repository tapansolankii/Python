# Question 6: First Non-Repeating Character
# Write a function to find the first non-repeating character in a string. 
# Return -1 if every character repeats.

def first_non_repeating_char(s):
    # Your code here
    # pass
    myDict = dict()
    for char in s:
        myDict[char] = myDict.get(char,0)+1

    for char in s:
        if myDict[char] == 1:
            return char

    return -1

# Example:
s = "swiss"
print(first_non_repeating_char(s))
# Output: 'w'

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\11_firstNonRepeatingCharacter.py
# w
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 