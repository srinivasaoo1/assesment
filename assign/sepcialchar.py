def count_characters(input_string):
    num_alphabets = 0
    num_digits = 0
    num_special_chars = 0

    for char in input_string:
        if char.isalpha():
            num_alphabets += 1
        elif char.isdigit():
            num_digits += 1
        else:
            num_special_chars += 1

    return num_alphabets, num_digits, num_special_chars

if __name__ == "__main__":
    input_string = input("Enter the string: ")

    alphabets, digits, special_chars = count_characters(input_string)

    print("Number of alphabets:", alphabets)
    print("Number of digits:", digits)
    print("Number of special characters:", special_chars)
