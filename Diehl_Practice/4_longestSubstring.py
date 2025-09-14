# Question 4: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without 
# repeating characters.

def length_of_longest_substring(s):
    # Your code here
    # pass
    maxLen = -float('inf')
    start = 0
    mySet = set()
    for end in range(len(s)):
        while s[end] in mySet:
            mySet.remove(s[start])
            start+=1
        mySet.add(s[end])
        maxLen = max(maxLen, end-start+1)
    return maxLen

# Example:
s = "abcabcbb"
print(length_of_longest_substring(s))  
# Output: 3 (substring "abc")


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\4_longestSubstring.py
# 3
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 