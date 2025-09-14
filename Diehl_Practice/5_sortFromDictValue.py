# Question 5: Custom Sorting
# Write a function to sort a list of dictionaries by a specific key.

def sort_by_key(lst, key):
    # Your code here
    # pass
    return sorted(lst, key=lambda x:x[key])

def sort_by_key_2(lst, key):
    n = len(lst)
    for i in range(n):
        for j in range(n-i-1):
            if lst[j][key] > lst[j+1][key]:
                lst[j],lst[j+1] = lst[j+1], lst[j]
    return lst

# Example:
lst = [{'name': 'Alice', 'age': 25}, {'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 23}]
key = 'age'
print(sort_by_key(lst, key))
print(sort_by_key_2(lst,key))


# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> py .\5_sortFromDictValue.py
# [{'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]
# [{'name': 'Bob', 'age': 22}, {'name': 'Charlie', 'age': 23}, {'name': 'Alice', 'age': 25}]
# PS D:\Yashwanth\HTW_Berlin\Self_Learnings\Python\Diehl_Practice> 