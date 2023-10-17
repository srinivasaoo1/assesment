class banker:
    def __init__(self):
        self.pin = ''
        self.balance = 0


        self.menu()
    def menu(self):
        user_input= input(''hello,
                          1 enter 1 to create pin
                          2 enter 2 to deposit
                          3 enter to withdraw
                          4 enter to check balance
                          5 enter 5 to exit'')
        if user_input == '1':
            self.create_pin()
        elif user_input =='2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            print('check balance')
        else:
            print('good bye')

    def create_pin(self):
        self.pin = input('enter your pin')
        print('pin created succesfully')
    def deposit(self):
        temp = input('enter your pin'):
        if temp == self.pin:
            amount = int('deposit amount')
            self.balance=self.balance+amount
            print('deposited sucessfully')
        else:
            print('invalid pin')
    def withdraw(self):
        temp = input('enter your pin')
        if temp == self.pin:
            amount = input('enter the withdrawal amount')
            if amount<self.balance:
              self.balance=self.balance-amount
              print('sucessfully withdraw')
            else:
                print('wrong pin')
        else:
            print('enter correct pin')
            
        
        


        