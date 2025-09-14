employee_file = open("employees.txt", "a")

print(employee_file.writable())
employee_file.write("\nKelly - Customer Service")

employee_file.close()


# Jim - Salesman
# Dwight - Salesman
# Pam - Receptionist
# Michael - Manager
# Oscar - Accountant
# Toby - Human Resources
# Toby - Human Resources
# Kelly - Customer Service
# Kelly - Customer Service