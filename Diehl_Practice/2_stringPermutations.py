# Question 2: String Permutations
# Write a function that returns all permutations of a given string.

from itertools import permutations

def string_permutations(s):
    # Your code here
    # pass
    perm = permutations(s)
    return [''.join(p) for p in perm]

def string_permutations_2(s):
    if len(s)==1:
        return s
    permutation = []
    for i, char in enumerate(s):
        remaining = s[:i]+s[i+1:]
        for perm in string_permutations_2(remaining):
            permutation.append(char + perm)
    return permutation

# Example:
s = "abc"
print(string_permutations(s))  
print(string_permutations_2(s))


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\2_stringPermutations.py
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 