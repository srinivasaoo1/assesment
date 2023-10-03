branches = {}

def employee_details():
    n = int(input('How many employee members '))

    for _ in range(n):
        name = input('Enter your name: ')
        email = input('Enter your email: ')
        employee_id = input('Enter your employee ID: ')
        branch = input('Enter your branch: ')

        emp_info = {
            'name': name,
            'email': email,
            'employee id': employee_id,
            'branch': branch
        }
        while any(emp['employee id'] == employee_id for emp in branches.get(branch, [])):
            print('Employee ID already exists in this branch. Please enter a new employee ID.')
            employee_id = input('Enter a new employee ID: ')

        emp_info['employee id'] = employee_id

        if branch in branches:
            branches[branch].append(emp_info)
        else:
            branches[branch] = [emp_info]

    print('Employee details:')
    for branch, employees in branches.items():
        print(f'{branch} branch: {len(employees)} employees')

employee_details()
