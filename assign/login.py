employee_dict = {}

def info_emp():
    a = int(input('Enter the number of employees: '))
    
    for i in range(1, a+1):
        name = input('Enter the name  ')
        domain = input('Enter the domain of emp: ')
        
        while True:
            email = input('Enter the email  ')
            if email.endswith('.com'):
                break
            else:
                print('Enter a valid email')
        
        while True:
            emp_id = input('enter the number')
            if emp_id.isalnum():
                break
            else:
                print('Enter a valid empl_id')
        
        if domain in employee_dict:
            employee_dict[domain].append({'name': name, 'email': email, 'emp_id': emp_id})
        else:
            employee_dict[domain] = [{'name': name, 'email': email, 'emp_id': emp_id}]

info_emp()

for domain in employee_dict.keys():
    print(domain)

enter_domain = input('Enter the domain : ')
if enter_domain in employee_dict:
    print(f'Domain details for "{enter_domain}":')
    for emp in employee_dict[enter_domain]:
        print(f"Name: {emp['name']}, Email: {emp['email']}, Employee ID: {emp['emp_id']}")
else:
    print('Details not found.')
