
details = {'srinivasa': 'srinivas123', 'hyderabad': 'telangana', 'andhra': 'pradesh'}

def login_details(username, password):
    if username in details and details[username] == password:
        print('You have successfully logged in')
    else:
        print('Details not found.')
        add_details = input('Do you want to add these details? (yes/no): ')
        if add_details.lower() == 'yes':
            add_new_details(username)
        else:
            print('Login failed.')

def add_new_details(username):
    new_password = input(f'Enter a password for {username}: ')
    details[username] = new_password
    print(f'New user {username} has been added with password: {new_password}')


user_1 = input('Enter the username: ')
pass_1 = input('Enter the password: ')
login_details(user_1, pass_1)