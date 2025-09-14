def longest_palindromic_substring (str):
    def expand_around_center(left, right):
        while left>=0 and right<len(str) and str[left]==str[right]:
            left-=1
            right+=1
        return str[left+1:right]
    
    string_longest=""
    for i in range(len(str)):
        odd = expand_around_center(i,i)
        even = expand_around_center(i,i+1)
        string_longest = max(string_longest, odd, even, key=len)
    return string_longest

str1 = "babad"
str2 = "cbbd"

print(longest_palindromic_substring(str1))
print(longest_palindromic_substring(str2))