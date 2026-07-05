import random
import string

print("------ Password Generator -------")

length = int(input("Enter password length: "))

use_upper = input("Include uppercase letters? (y/n): ").lower()
use_lower = input("Include lowercase letters? (y/n): ").lower()
use_digits = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include special characters? (y/n): ").lower()

characters = ""

if use_upper == "y":
    characters += string.ascii_uppercase

if use_lower == "y":
    characters += string.ascii_lowercase

if use_digits == "y":
    characters += string.digits

if use_symbols == "y":
    characters += string.punctuation

if characters == "":
    print("You must select at least one character type.")
else:
    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:")
    print(password)

    strength = 0

if length >=8:
    strength+=1

if use_upper == "y":
    strength += 1

if use_lower == "y":
    strength += 1

if use_digits == "y":
    strength += 1

if use_symbols == "y":
    strength += 1

if strength == 5:
    print("Password Strength: Strong ")
elif strength >= 2:
    print("Password Strength: Moderate ")
else:
    print("Password Strength: Weak ")