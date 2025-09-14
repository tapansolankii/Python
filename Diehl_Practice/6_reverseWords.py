# Question 1: Reverse Words in a String
# Write a function that takes a string as input and 
# returns the string with the words reversed.


def reverse_words(s: str):
    # Your code here
    # pass
    words = s.split(' ')
    words.reverse()
    return [' '.join(words)]

# Example:
s = "The quick brown fox"
print(reverse_words(s))


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\6_reverseWords.py
# ['fox brown quick The']
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 
