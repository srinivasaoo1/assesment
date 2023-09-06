numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
odd_numbers =filter(lambda x: x%2 != 0, numbers)
even_numbers_list = list(even_numbers)
odd_numbers_list =list(odd_numbers)
print('Even numbers:', even_numbers_list)
print('Odd numbers:', odd_numbers_list)
