# Question 5: Anagram Checker
# Write a function that checks if two strings are anagrams of each other.


def are_anagrams(str1, str2):
    # Your code here
    # pass
    if len(str1) != len(str2):
        return False
    dict1 = {}
    dict2 = {}
    for i in range(len(str1)):
        dict1[str1[i]] = dict1.get(str1[i],0)+1
        dict2[str2[i]] = dict2.get(str2[i],0)+1
    if dict1==dict2:
        return True
    return False

def are_anagrams_2(str1, str2):
    return sorted(str1) == sorted(str2)

# Example:
str1 = "listen"
str2 = "silent"
print(are_anagrams(str1, str2))
print(are_anagrams_2(str1, str2))
# Output: True

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\10_checkAnagrams.py
# True
# True
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 