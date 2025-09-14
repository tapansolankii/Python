name = int(input("Enter your name: "))
# print("Hello " + name + ". Nice to Meet you!")
# will give an error
print(f"Hello {name}. Nice to meet you")
# but f string doesn't

print(type(name))


num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
# or use float for decimal

print(result)