def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

print("Start")
greet_user(last_name="Smith", first_name="John")
# keyword arguments
print("Finish")

greet_user("Smith", last_name="John")
# Keyword arguments should always come after positional arguments.

# By default, all functions in python return None 
# Usually, your function should not ask any input from user
# or print anything. For reusability in other files.