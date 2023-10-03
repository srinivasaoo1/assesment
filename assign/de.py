def sort_ele():
    elements = []
    n = int(input('enter the number'))
    for i in range(n):

     name = input('Enter the name: ')
     empid = input('Enter the ID: ')
     email = input('Enter the email: ')
     domain = input('enter the domain')

     elements.append((name,email,empid,domain))
     elements_sorted = sorted(elements, key = lambda x:x[0])
     print(elements_sorted)
sort_ele()