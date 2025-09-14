employee_file = open("employees.txt", "r")
# a is append at end. w is write anywhere.
# r+ read and write

print(employee_file.readable())
# if employee_file.readable():
#     print(employee_file.read())

print(employee_file.readline())
print(employee_file.readline())
# print(employee_file.readlines()[0]) 
# readlines reads all the lines
# even if you are accessing only the first element

print("///////////////")

for employee in employee_file.readlines():
    print(employee)

employee_file.close()