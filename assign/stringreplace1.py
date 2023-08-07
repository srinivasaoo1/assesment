def replace_spaces(input_string, replacement_char):
    return input_string.replace(' ', replacement_char)

if __name__ == "__main__":
    input_string = input("Enter the input string: ")
    replacement_char = input("Enter the replacement character: ")

    result_string = replace_spaces(input_string, replacement_char)
    print("Result:", result_string)
