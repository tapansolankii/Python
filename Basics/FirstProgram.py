print(4+5)
x=1
if x==1:
    print("Yes x is 1")
else:
    print("x is not 1")

myFloat = 7.0
print(myFloat)
myFloat = float(7)
print(myFloat)

mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

a, b = 3, 4
print(a, b)

if isinstance(myFloat, float) and myFloat == 7.0:
    print("YESS")

mylist = []
print(mylist)
mylist.append(1)
print(mylist)
mylist.append(2)
mylist.append(3)
print("Hiiii")
print(mylist)
for x in mylist:
    x=x*3
print(mylist)

lotsofhellos = "hello" * 10
print(lotsofhellos)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

print([1,2,3] * 3)

x = object()
print(type(x))

originalList = [1,2,3,4,5]
squaredList = [x**2 for x in originalList]
print(squaredList)
print("...................................")

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
print("...................................")

name = "Yashwanth"
age = 23
print("Hello %s!, you are %d years old" % (name, age))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
print(data[1])
print("************************************")
astring = "Hello world!"
print(astring.count("l"))
print(astring.index("rl"))
print(astring[3:7])
#print(astring.index("yyyyyy"))
print(astring.index("lo"))

"""
This is a comment
written in
more than just one line
"""

print("*****************")
astring = "Hemlo wtrud!"
print(astring[3:11:2])
print(astring[::-1])
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
afewwords = astring.split("m")
print(afewwords)

List = []
print("Initial blank List: ")
print(List)
List = ['GeeksForGeeks']
print("\nList with the use of String: ")
print(List)
List = ["Geeks", "For", "Geeks"]
print("\nList containing multiple values: ")
print(List[0])
print(List[2])
List = [['Geeks', 'For'], ['Geeks']]
print("\nMulti-Dimensional List: ")
print(List)

print("&&&&&&&&&&&&&&&&&&&&&&&&")
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())
print("....................")
# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

x = s.split(" ")
print("%s" % x)

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
f = ["John", "Rick"]
if name in f:
    print("YESSS")

print(">>>>>>>>>>>>>>>>>>>>>>>>>>")
# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x, end = " ")

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)

print(">>>>>>>>>>")
count = 0
while True:
    print(count, end=" ")
    count += 1
    if count >= 5:
        break
print("\n")
# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x, end=" ")

print("YYYYYYYYYYYYYYY")
count = 0
while count < 5:
    print(count)
    count += 1

# Prints out 0,1,2,3,4
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

'''
#When the loop condition of "for" or "while" statement 
fails then code part in "else" is executed. If a break 
statement is executed inside the for loop then the "else" 
part is skipped. Note that the "else" part is executed 
even if there is a continue statement.
'''
print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
# Prints out 0,1,2,3,4 and then it 
#prints "count value reached 5"
count=0
while(count<5):
    count+=1
    if count%2==0:
        continue
    print(count)
else:
    print("count value reached %d" %(count))