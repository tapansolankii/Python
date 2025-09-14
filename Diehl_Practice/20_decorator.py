def decorator(func):
    def wrapper():
        print(f'Before func was called.')
        func()
        print(f'After func is called.')
    return wrapper


@decorator
def myFunction():
    print(f'I am a function!!')


# /////////////////

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} called with {args} and {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_decorator
def add(a, b):
    return a + b

# ///////////////////////

def access_control(role):
    def decorator(func):
        def wrapper(user_role):
            if (user_role==role):
                return func()
            else:
                print(f'Access deined')
        return wrapper
    return decorator

@access_control("admin")
def some_function():
    print("Access control testing. This is a secret function")

# ////////////////////////

def input_checking(func):
    def wrapper(x):
        if x<0:
            # raise ValueError('x cannot be negative')
            print(f"x cant be negative")
        else:
            return func(x)
    return wrapper
        
@input_checking
def square_root(x):
    print(x**0.5)


if __name__ == '__main__':
    myFunction()
    add(4,5)
    print()
    some_function("admin")
    some_function("user")
    print()
    square_root(9)
    square_root(-1)


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\20_decorator.py
# Before func was called.
# I am a function!!
# After func is called.
# Function add called with (4, 5) and {}

# Access control testing. This is a secret function
# Access deined

# 3.0
# x cant be negative
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 