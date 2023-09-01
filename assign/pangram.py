def is_pangram(input_string):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")
    input_string = ''.join(filter(str.isalpha, input_string)).lower()
    unique_letters = set(input_string)
    return unique_letters == alphabet_set

sample_string = input('enter the string:')
result = is_pangram(sample_string)

if result:
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")

