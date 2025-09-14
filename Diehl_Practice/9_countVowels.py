# Question 4: Count Vowels in a String
# Write a function that counts the number of vowels in a given string.


def count_vowels(s):
    # Your code here
    # pass
    vowels = "aeiouAEIOU"
    count=0
    for char in s:
        if char in vowels:
            count+=1
    return count

# Example:
s = "hello world"
print(count_vowels(s))
# Output: 3
