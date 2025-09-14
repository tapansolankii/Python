fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

for i in range(0, 10, 2):  # Start=0, Stop=10, Step=2
    print(i)

text = "hello"
for char in text:
    print(char)

# enumerate for lists
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Dictionaries
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# Zip for 2 or more
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# For else loop
# The else block runs if the loop exits normally (i.e., without hitting a break).
numbers = [1, 2, 3, 4]
for number in numbers:
    if number == 5:
        print("Found 5!")
        break
else:
    print("5 was not found.")


# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)

# Reverse
for i in reversed(range(5)):
    print(i)


for i in range(5):
    if i == 2:
        continue  # Skip this iteration
    if i == 4:
        break  # Exit the loop
    print(i)

# Sets
unique_numbers = {1, 2, 3, 4}
for num in unique_numbers:
    print(num)

# Tuples
colors = ("red", "green", "blue")
for color in colors:
    print(color)

# each letter in each word
friends = ["Jim", "Karen", "Linda"]
for friend in friends:
    for letter in friend:
        print(letter)
    print()

for index in range(len(friends)):
    print(friends[index])