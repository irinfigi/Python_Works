import re

def is_strong_password(password):
    """
    Validates whether a password is strong based on the given criteria:
    - At least 8 characters long
    - Contains one uppercase character
    - Contains one lowercase character
    - Contains at least one digit
    - Contains at least one special character
    """
    # Check for minimum length of 8 characters
    if len(password) < 8:
        return False
    
    # Compile regular expressions for each condition
    uppercase_regex = re.compile(r'[A-Z]')
    lowercase_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'\d')
    special_char_regex = re.compile(r'[\W_]')  # \W matches any non-word character, _ is included to cover all special chars
    
    # Check conditions
    if (not uppercase_regex.search(password)):
        return False
    if (not lowercase_regex.search(password)):
        return False
    if (not digit_regex.search(password)):
        return False
    if (not special_char_regex.search(password)):
        return False
    
    # If all conditions are met
    return True

# Example usage:
password = "Example1@"
print("Password is strong:", is_strong_password(password))
