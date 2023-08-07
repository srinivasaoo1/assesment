def check_vowel_or_consonant(character):
    vowels = "aeiouAEIOU"
    
    if character.isalpha():
        if character in vowels:
            return "Vowel"
        else:
            return "Consonant"
    else:
        return "Not a valid alphabet."

if __name__ == "__main__":
    input_character = input("Enter a character: ")

    result = check_vowel_or_consonant(input_character)
    print(f"The character '{input_character}' is a {result}.")

