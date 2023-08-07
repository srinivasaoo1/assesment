def custom_sort(input_string):
    alphabets = []
    digits = []

    # Split the characters into alphabets and digits
    for char in input_string:
        if char.isalpha():
            alphabets.append(char)
        elif char.isdigit():
            digits.append(char)

    # Sort the alphabets and digits separately
    sorted_alphabets = sorted(alphabets)
    sorted_digits = sorted(digits)

    # Combine the sorted alphabets and digits
    sorted_string = ''.join(sorted_alphabets + sorted_digits)

    return sorted_string

if __name__ == "__main__":
    input_string = input("Enter the string: ")

    sorted_string = custom_sort(input_string)
    print("Sorted string (Alphabets first, then Numeric values):", sorted_string)
