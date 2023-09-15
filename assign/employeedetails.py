emp_list = []

n = int(input("Enter the number of employees: "))
count = 0

while count < n:
    emp = {}
    emp['Domain'] = input("Enter the employee's domain: ")
    emp['Name'] = input("Enter the employee's name: ")
    emp['EmpID'] = input("Enter the employee's empid: ")
    emp['Email'] = input("Enter the employee's email: ")
    emp_list.append(emp)
    print('Employee details added successfully!')
    count += 1

print("\nEmployee Details:")

count = 1

while count <= n:
    emp = emp_list[count - 1]
    print(f"Employee {count}:")
    for key, value in emp.items():
        print(f"{key}: {value}")
    print()
    count += 1