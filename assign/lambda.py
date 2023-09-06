s = lambda a : a ** 2
add = lambda a,b : a + b
mul = lambda a,b : a * b
a = int(input('enter the value'))
b = int(input('enter the value'))
s_result = s(a)
add_result = add(a,b)
mul_result = mul(a,b)
print(f'the square of {a} is {s_result}')
print(f'the addition of two numbers is {add_result}')
print(f'the mul of two number is {mul_result}')
