def fibonacci_series(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_series(n - 1) + fibonacci_series(n - 2)

n = int(input('Enter the value: '))

if n <= 0:
    print('Fibonacci series does not occur for non-positive numbers.')
else:
    print('Fibonacci series:')
    for i in range(n + 1):
        fibo = fibonacci_series(i)
        print(f'The Fibonacci number at position {i} is {fibo}')

