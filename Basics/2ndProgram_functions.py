def myFunction():
    print("Hello!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

myFunction()
username = "Yashwanth"
greeting = "What's up?"
my_function_with_args(username,greeting)
x = sum_two_numbers(1,2)
print(x)
print(sum_two_numbers(1,2))

# Modify this function to return a list of strings as defined above
def list_benefits():
    return "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    #print(list_of_benefits)
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

'''
list_of_benefits = list_benefits()
print(list_of_benefits)
'''
print("*****************")

#Classes
class MyClass:
    variable = "Anusha"

    def function(self):
        print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()
myobjecty.variable = "Yashwanth"
print(myobjectx.variable)
print(myobjecty.variable)
myobjecty.function()

print("#####################")
class NumberHolder:
    #def __init__(self) -> None:
    #    pass
    def __init__(self, number):
        self.number = number
    
    def returnNumber(self):
        return self.number

y=NumberHolder(42)
print(y.returnNumber())

print("$$$$$$$$$$$$$$$$$$$$$")
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1=Vehicle()
car1.name="Fer"
car1.color="red"
car1.value=60000
car1.kind="convertible"
print(car1.description())

print("^^^^^^^^^^^^^^^^^^^")
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
print("...")
del phonebook["John"]
phonebook.pop("Jill")
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

phonebook["Jake"]=938273443
#phonebook.pop("Jill")
# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
    
if "Jill" not in phonebook:      
    print("Jill is not listed in the phonebook.")

'''
# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()
'''

#Importing from other modules
'''
from draw import draw_game
or
from draw import *

def main():
    result = play_game()
    draw_game(result)
'''

#Importing 2 modules with same name
'''
# game.py
# import the draw module
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)
'''

'''
when importing a module, a .pyc file is created. 
This is a compiled Python file. Python compiles 
files into Python bytecode so that it won't have 
to parse the files each time modules are loaded. 
If a .pyc file exists, it gets loaded instead of 
the .py file. This process is transparent to the user.
'''

#Defining path of modules
'''
PYTHONPATH=/foo python game.py
sys.path.append("/foo")
'''

'''
# import the library
import urllib

# use it
urllib.urlopen(...)

help(urllib.urlopen)
'''

'''
The __init__.py file can also decide which modules 
the package exports as the API, while keeping other 
modules internal, by overriding the __all__ variable 
like so:
__init__.py:
__all__ = ["bar"]
'''

'''
import re

find_members=[]
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))
'''
