
def intro(name, age):
    print(f"Hello {name}. You are {age}")
    print("hello" + name + ". You are" + str(age) + "years old.")


intro("Anusha", 25)

def cube(num) -> int:
    return num**3
    print(f"This won't be printed")

print(cube(3))


isMale = True
isTall = False

if isMale and isTall:
    print(f"You are a tall male")
elif isMale and not(isTall):
    print(f"You are a short male")
elif not(isMale) and isTall:
    print(f"You are a tall female")
else:
    print(f"You are not tall and not a male.")


def maxNum(num1, num2, num3):
    # return num1>=num2 ? (num1>=num3 ? num1 : num3) : (num2>=num3 ? num2 : num3)
    return num1 if num1>=num2 and num1>=num3 else num2 if num2>=num3 else num3


print(maxNum(200,40,6))

a = 100
b = 20
c = a if a>b else b
print(c)


def check_even_odd(num) -> int:
    return "Odd" if num%2 else "Even"

print(check_even_odd(7))  # Output: Odd