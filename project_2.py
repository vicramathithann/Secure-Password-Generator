#!/usr/bin/env python3
import secrets
import string


# -------------------------------
# Password Strength Checker
# -------------------------------

def check_password(password):
    length = len(password)

    upper = any(ch.isupper() for ch in password)
    lower = any(ch.islower() for ch in password)
    number = any(ch.isdigit() for ch in password)
    symbol = any(ch in string.punctuation for ch in password)

    score = sum([upper, lower, number, symbol])

    print("\n========== PASSWORD ANALYSIS ==========")
    print(f"Password Length : {length}")
    print(f"Uppercase       : {'Yes' if upper else 'No'}")
    print(f"Lowercase       : {'Yes' if lower else 'No'}")
    print(f"Number          : {'Yes' if number else 'No'}")
    print(f"Symbol          : {'Yes' if symbol else 'No'}")

    # Strength calculation
    if length < 6:
        strength = "Very Weak"
    elif length < 8:
        strength = "Weak"
    elif score == 4 and length >= 12:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print(f"\nPassword Strength: {strength}")

    # Show missing requirements
    if length < 8:
        print("Missing: Password should contain at least 8 characters.")

    if not upper:
        print("Missing: Uppercase letter")

    if not lower:
        print("Missing: Lowercase letter")

    if not number:
        print("Missing: Number")

    if not symbol:
        print("Missing: Special symbol")

    return strength


# -------------------------------
# Secure Password Generator
# -------------------------------

def generate_password(length):
    if length < 8:
        print("Password length should be at least 8.")
        return

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    # Guarantee at least one of each
    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]

    # Remaining characters
    all_characters = uppercase + lowercase + numbers + symbols

    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Secure shuffle
    secrets.SystemRandom().shuffle(password)

    password = "".join(password)

    print("\n========== GENERATED PASSWORD ==========")
    print(password)
    print(f"Length: {len(password)}")

    return password


# -------------------------------
# Main Tool
# -------------------------------

def main():

    while True:

        print("\n================================")
        print("       PASSWORD SECURITY TOOL")
        print("================================")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        # Check password
        if choice == "1":

            password = input("\nEnter your password: ")

            if password:
                check_password(password)
            else:
                print("Password cannot be empty.")

        # Generate password
        elif choice == "2":

            try:
                length = int(
                    input("Enter password length (minimum 8): ")
                )

                generate_password(length)

            except ValueError:
                print("Please enter a valid number.")

        # Exit
        elif choice == "3":

            print("\nThank you for using Password Security Tool.")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")


# Start program
if __name__ == "__main__":
    main()
