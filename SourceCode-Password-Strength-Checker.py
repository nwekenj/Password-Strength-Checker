import re

def check_password_strength(password):
    # Initialize strength to 0
    strength = 0

    # Check password length
    if len(password) >= 8:
        strength += 1

    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        strength += 1

    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        strength += 1

    # Check for digit
    if re.search(r'\d', password):
        strength += 1

    # Check for special character
    if re.search(r'\W', password):
        strength += 1

    # Rate password strength
    if strength <= 2:
        return 'Weak'
    elif strength == 3 or strength == 4:
        return 'Medium'
    else:
        return 'Strong'

# Get user input
password = input("Enter a password to test: ")

# Test the function
print(check_password_strength(password))