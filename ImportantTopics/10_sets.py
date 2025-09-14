my_set = {1, 2, 3}

empty_set = {}

my_set = {1, 2}
my_set.add(3)
# add 1 element

print(my_set)


my_set.update([3, 4], {5, 6})
# add multiple
print(my_set)


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\ImportantTopics> py .\10_sets.py
# {1, 2, 3}
# {1, 2, 3, 4, 5, 6}







# remove() - Removes a specific element (Raises an error if not found)
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # {1, 3}

# b. discard() - Removes a specific element (No error if not found)
my_set = {1, 2, 3}
my_set.discard(4)  # No error if 4 is not in the set
print(my_set)  # {1, 2, 3}



# c. pop() - Removes and returns a random element
my_set = {1, 2, 3}
print(my_set.pop())  # Removes a random element


# d. clear() - Removes all elements
my_set = {1, 2, 3}
my_set.clear()
print(my_set)  # set()










set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)           # {1, 2, 3, 4, 5}
print(set1.union(set2))      # {1, 2, 3, 4, 5}



print(set1 & set2)               # {3}
print(set1.intersection(set2))   # {3}



print(set1 - set2)               # {1, 2}
print(set1.difference(set2))     # {1, 2}

# elements not common in both sets.
print(set1 ^ set2)                          # {1, 2, 4, 5}
print(set1.symmetric_difference(set2))      # {1, 2, 4, 5}


set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1 <= set2)               # True
print(set1.issubset(set2))        # True


print(set2 >= set1)               # True
print(set2.issuperset(set1))      # True



# Disjoint (isdisjoint()) - Checks if two sets have no elements in common
set3 = {7, 8}
print(set1.isdisjoint(set3))  # True



set1 = {1, 2, 3}
set2 = set1.copy()
print(set2)  # {1, 2, 3}




print(len(set2))







my_set = {1, 2, 3}
print(2 in my_set)     # True
print(4 not in my_set) # True



fs = frozenset([1, 2, 3])
print(fs)  # frozenset({1, 2, 3})
# fs.add(4)  # Error! Cannot add to a frozen set
