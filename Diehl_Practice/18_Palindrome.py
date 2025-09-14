def is_palindrome(s: str):
    # Your code here
    # pass
    start, end = 0, len(s)-1
    s = s.lower()
    print(s)
    invalid = " 0123456789,:"
    while start<end:
        while s[start] in invalid:
            start+=1
        while s[end] in invalid:
            end-=1
        if s[start] == s[end]:
            start+=1
            end-=1
        else:
            return False
    return True

# Example:
s = "A man, a plan, a canal: Panama"
print(is_palindrome(s))
# Output: True

# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\18_Palindrome.py
# a man, a plan, a canal: panama
# True
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 

# Complexity:
# Time Complexity: 𝑂(𝑛), where n is the length of the string. 
# Each character is processed once.
# Space Complexity: 𝑂(1), as no additional data structures 
# are used.


# ChatGPT
# def is_palindrome(s: str) -> bool:
#     # Two pointers
#     start, end = 0, len(s) - 1
#     s = s.lower()  # Convert string to lowercase for case insensitivity

#     while start < end:
#         # Skip non-alphanumeric characters
#         while start < end and not s[start].isalnum():
#             start += 1
#         while start < end and not s[end].isalnum():
#             end -= 1

#         # Check for mismatch
#         if s[start] != s[end]:
#             return False

#         # Move pointers
#         start += 1
#         end -= 1

#     return True