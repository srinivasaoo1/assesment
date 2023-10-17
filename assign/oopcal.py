class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "enter other than zero"
cal = Calculator()
print("Choose an operation:")
print("1.add")
print("2. Sub")
print("3. Multiply")
print("4. Divide")

choice = input("Enter the number of the operation you want to perform: ")
x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
if choice == "1":
    result = cal.add(x, y)
    print(result)
elif choice == "2":
    result = cal.subtract(x, y)
    print(result)
elif choice == "3":
    result = cal.multiply(x, y)
    print(result)
elif choice == "4":
    result = cal.divide(x, y)
    print(result)
else:
    print("Invalid")