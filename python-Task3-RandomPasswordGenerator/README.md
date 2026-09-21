
## OIBSIP Task 3

A simple Python command-line Random Password Generator developed as part of the Oasis Infobyte Python Programming Internship.

## Features

- Allows the user to choose the password length.
- Minimum password length of 8 characters.
- Supports uppercase letters.
- Supports lowercase letters.
- Supports numbers.
- Supports symbols.
- Requires at least 2 character types.
- Validates invalid inputs.
- Generates a password containing the selected character types.
- Allows the user to generate another password without restarting the program.

## Technologies Used

- Python
- random module
- string module
- input()
- Conditional statements
- Exception handling

## How to Run

1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Open `password_generator.py`.
4. Run the program.
5. Enter a password length of at least 8.
6. Select at least 2 character types.
7. The program generates a random password.

## Character Types

| Option | Character Type |
|---|---|
| 1 | Uppercase letters |
| 2 | Lowercase letters |
| 3 | Numbers |
| 4 | Symbols |

## Example

```text
Enter password length (minimum 8): 12

Choose character types:
1. Uppercase letters
2. Lowercase letters
3. Numbers
4. Symbols

Enter your choices (example: 123): 1234

Generated Password: A7@kP2!xQ9#m
