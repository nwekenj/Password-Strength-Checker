# Password-Strength-Checker
A Python script that checks and rates the strength of a password based on certain criteria such as length, presence of uppercase and lowercase letters, and digits.

# Password Strength Checker

This project contains a Python script that evaluates the strength of a password based on several key criteria. It's a simple yet powerful tool that can help users create passwords that are secure and robust.

## Features

The `check_password_strength` function in the script evaluates a password based on the following criteria:

1. **Length**: The password must be at least 8 characters long.
2. **Uppercase Letter**: The password must contain at least one uppercase letter.
3. **Lowercase Letter**: The password must contain at least one lowercase letter.
4. **Digit**: The password must contain at least one digit.

For each criterion the password meets, the strength score is incremented by 1. The function then returns a strength rating ('Weak', 'Medium', or 'Strong') based on the final strength score.

## Usage

To use this script, simply call the `check_password_strength` function with a password as the argument. The function will return the strength rating of the password.

Example:

```python
print(check_password_strength('Test@123'))  # Outputs: Strong
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
