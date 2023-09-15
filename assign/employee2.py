employee_details_list = []
def add_employee():
    employee = {}
    employee['Domain'] = input("Enter the employee's domain: ")
    employee['Name'] = input("Enter the employee's name: ")
    employee['EmpID'] = input("Enter the employee's empid: ")
    employee['Email'] = input("Enter the employee's email: ")
    employee_details_list.append(employee)
    print('Employee details added successfully!')
def print_all_employee_details():
    print("\nEmployee Details:")
    for i, employee in enumerate(employee_details_list, start=1):
        print(f"Employee {i}:")
        for key, value in employee.items():
            print(f"{key}: {value}")
        print()
n = int(input("Enter the number of employees: "))
for _ in range(n):
    add_employee()
print_all_employee_details()