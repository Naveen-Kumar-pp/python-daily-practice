"""
Password Strength Validator
Conditions:
1. Minimum 8 characters
2. At least one uppercase letter
3. At least one digit
4. At least one special character
"""

password = input("Enter your password: ")

has_min_length = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_uppercase = any(char.isupper() for char in password)
has_special = any(not char.isalnum() for char in password)

if has_min_length and has_digit and has_uppercase and has_special:
    print("Strong Password")
else:
    print("Weak Password")
