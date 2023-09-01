def count_upper_lower_case_letters(input_string):
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

sample_string = input('enter the value:')
upper_count, lower_count = count_upper_lower_case_letters(sample_string)

print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
