try:
    x = int(input("Enter a number: "))
    print(x)
except:
    print(f"Invalid input")

# try:
#     value = 10/0
# except ZeroDivisionError:
#     print(f"Divided by 0")
# except ValueError:
#     print(f"Invalid input")

try:
    value = 10/0
except ZeroDivisionError as err:
    print(f"{err}")
except ValueError:
    print(f"Invalid input")