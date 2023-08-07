def remove_spaces(input_string):
    return input_string.replace(" ", "")

if __name__ == "__main__":
    input_string = input("Enter the string: ")

    result_string = remove_spaces(input_string)
    print("String after removing spaces:", result_string)
