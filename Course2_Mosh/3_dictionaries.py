numbers = {
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four",
    "5":"Five"
}

value = input("Enter a phone number: ")
# for val in value:
#     print(f'{numbers[val]}\t')

output = ""
for val in value:
    output += numbers.get(val, "!") + " "
print(output)