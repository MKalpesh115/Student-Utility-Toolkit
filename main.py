"""A beginner-friendly collection of useful student tools."""

import random
import string


def calculator():
    """Perform a basic arithmetic operation on two numbers."""
    print("\nCalculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = input("Choose an operation (1-4): ").strip()
    if operation not in {"1", "2", "3", "4"}:
        print("Invalid operation. Please choose a number from 1 to 4.")
        return

    try:
        first_number = float(input("Enter the first number: "))
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if operation == "1":
        result = first_number + second_number
    elif operation == "2":
        result = first_number - second_number
    elif operation == "3":
        result = first_number * second_number
    else:
        if second_number == 0:
            print("Division by zero is not allowed.")
            return
        result = first_number / second_number

    print(f"Result: {result}")


def temperature_converter():
    """Convert a temperature between Celsius and Fahrenheit."""
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    conversion = input("Choose a conversion (1-2): ").strip()
    if conversion not in {"1", "2"}:
        print("Invalid choice. Please choose 1 or 2.")
        return

    try:
        temperature = float(input("Enter the temperature: "))
    except ValueError:
        print("Please enter a valid temperature.")
        return

    if conversion == "1":
        converted = (temperature * 9 / 5) + 32
        print(f"{temperature} Celsius is {converted:.2f} Fahrenheit.")
    else:
        converted = (temperature - 32) * 5 / 9
        print(f"{temperature} Fahrenheit is {converted:.2f} Celsius.")


def word_counter():
    """Count the words and characters in a sentence."""
    print("\nWord Counter")
    sentence = input("Enter a sentence: ")

    # Splitting on whitespace avoids counting repeated spaces as extra words.
    word_count = len(sentence.split())
    character_count = len(sentence)
    print(f"Words: {word_count}")
    print(f"Characters (including spaces): {character_count}")


def password_generator():
    """Generate a random password containing each required character type."""
    print("\nPassword Generator")
    try:
        length = int(input("Enter the password length (at least 3): "))
    except ValueError:
        print("Please enter a whole number.")
        return

    if length < 3:
        print("Password length must be at least 3 to include all character types.")
        return

    character_groups = [
        string.ascii_letters,
        string.digits,
        string.punctuation,
    ]

    # Start with one character from each group, then fill and shuffle the password.
    password_characters = [random.choice(group) for group in character_groups]
    all_characters = "".join(character_groups)
    password_characters.extend(
        random.choice(all_characters) for _ in range(length - len(password_characters))
    )
    random.shuffle(password_characters)

    print(f"Your password: {''.join(password_characters)}")


def main():
    """Display the main menu and run the selected tool."""
    while True:
        print("\n=== Student Utility Toolkit ===")
        print("1. Calculator")
        print("2. Temperature Converter")
        print("3. Word Counter")
        print("4. Password Generator")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            temperature_converter()
        elif choice == "3":
            word_counter()
        elif choice == "4":
            password_generator()
        elif choice == "5":
            print("Thank you for using Student Utility Toolkit. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
