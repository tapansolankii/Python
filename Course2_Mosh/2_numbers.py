import math

# x=10
# x+=3
# # augmented assignment operator
# x = 10 + 3 * 2 ** 2
# # first power , then bodmas

# print(math.ceil(2.9))

# for item in range(10):
#     print(item)
# # prints 0 to 9

# for item in range(5, 10, 2):
#     print(item)
# # prints 5, 7, 9

# numbers = [5,2,5,2,2]
# for number in numbers:
#     print('*' * number)

# numbers.append(20)
# # at end of list
# numbers.insert(0, 35)
# # at beginning of list coz of 0
# numbers.remove(2)
# # removes the element 2
# numbers.clear()
# # removes all the elements but numbers list is still present
# numbers.pop()
# # remove last item
# numbers.index(2)
# # returns the first index of this item. 
# # If it doesn't exist, program will give a value error.
# print(50 in numbers)
# # returns False
# print(numbers.count(5))
# # total times 5 is present
# numbers.sort()
# numbers.reverse()
# number2 = numbers.copy()

# uniques =[]
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)


# names = ["John", "Sarah", "mary", "yasee", "aerg"]







# Tuples
# only have count and index methods available
# All methods which start with '__' are magic methods

# unpacking
# coordinates = (3,5,4)
# x, y, z = coordinates
# print(x*y*z)








# Dictionaries
customer = {
    "name" : "John Smith",
    "age" : 25,
    "is_verified" : True
}

# print(customer["name"])
# print(customer["nameergerg"])
# gives a key error
print(customer.get("namergtrrt"))
# returns None - safer. None is an object that represents absence of value
print(customer.get("drggrstsh", -1))
# Can also give a value that we want (here, -1)

customer["age"] = 37