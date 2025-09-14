message = input("Enter a word with emoji: ")
words = message.split(' ')
print(words)

emoji = {
    ":)": "HAPPY",
    ":(": "SAD",
}

output =""
for word in words:
    output+=emoji.get(word, word) + " "

print(output)

# Output
# Enter a word with emoji: erhr r :) :(
# ['erhr', 'r', ':)', ':(']
# erhr r HAPPY SAD 






# Functions
# ARGUMENTS are actual information
# PARAMETERS are information that you pass