count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# break
count = 0
while True:
    print(f"Count is {count}")
    count += 1
    if count >= 5:
        break

# continue
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(f"Count is {count}")

# while else
# The else block runs if the loop exits normally (i.e., without hitting a break).
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1
else:
    print("Loop completed without break.")

# Output
# Count is 0
# Count is 1
# Count is 2
# Count is 3
# Count is 4
# Loop completed without break.


while True:
    user_input = input("Type 'exit' to quit: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break

# Type 'exit' to quit: hello
# Type 'exit' to quit: exit
# Goodbye!

a, b = 0, 5
while a < 5 and b > 0:
    print(f"a={a}, b={b}")
    a += 1
    b -= 1

# Python doesn't have a do while loop
# Do while loop simulation
count = 0
while True:
    print(f"Count is {count}")
    count += 1
    if count >= 5:
        break

# Nested
i = 0
while i < 3:
    j = 0
    while j < 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# counting down
count = 5
while count > 0:
    print(f"Count is {count}")
    count -= 1

# Input Validation
age = 0
while age <= 0:
    try:
        age = int(input("Enter a valid age (greater than 0): "))
    except ValueError:
        print("Please enter a number.")

# File
with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

# Timer
import time
count = 5
while count > 0:
    print(f"Time left: {count} seconds")
    time.sleep(1)
    count -= 1
print("Time's up!")
# Every 1 second it gives out an output