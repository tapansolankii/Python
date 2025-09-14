s = "cateigoluh"
result = ""

for c in s:
    if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
        result+='g'
    else:
        result+=c
print(result)

# if(letter in "aeiouAEIOU")
# or
# if letter.lower() in "aeiou":
    # if letter.isupper():
    #     result+='G'
    # else:
    #     result+='g'