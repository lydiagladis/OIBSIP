# Random Password Generator
# Oasis Infobyte Internship - Task 3

import random
import string

print("===== RANDOM PASSWORD GENERATOR =====")

while True:
    try:
        # Ask for password length
        length = int(input("\nEnter password length (minimum 8): "))

        # Check minimum length
        if length < 8:
            print("Error: Password length must be at least 8.")
            continue

        # Display character type options
        print("\nChoose character types:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        # Ask user for character types
        choices = input("Enter your choices (example: 123): ")

        # Check for valid choices
        valid_choices = set("1234")
        choices = set(choices) & valid_choices

        # At least 2 types must be selected
        if len(choices) < 2:
            print("Error: Please select at least 2 character types.")
            continue

        # Convert set back to string
        choices = "".join(choices)

        # Create character pool
        characters = ""

        if "1" in choices:
            characters += string.ascii_uppercase

        if "2" in choices:
            characters += string.ascii_lowercase

        if "3" in choices:
            characters += string.digits

        if "4" in choices:
            characters += string.punctuation

        # Generate password
        password = ""

        for i in range(length):
            password += random.choice(characters)

        # Display password
        print("\n===== GENERATED PASSWORD =====")
        print("Password:", password)

        # Ask whether to generate another password
        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("\nThank you for using the Password Generator!")
            break

    except ValueError:
        print("Error: Please enter a valid number.")
