try:
    age = int(input("Enter your age: "))
    income = 20000
    risk = income/age
except ValueError:
    print("Invalid value")
except ZeroDivisionError:
    print("Age can't be 0")