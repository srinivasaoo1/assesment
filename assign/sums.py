def list(input_list):
    total = 0

    for number in input_list:
        total += number

    return total

numbers = eval(input('the the list of numbers'))
result = list(numbers)
print("Sum of numbers in the list:", result)
