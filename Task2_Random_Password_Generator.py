import random

# Character sets
lowercase_chars = "abcdefghijklmnopqrstuvwxyz"
uppercase_chars = lowercase_chars.upper()
digits = "0123456789"
symbols = "!@#$%^&*()"

def get_user_choice(prompt, valid_options):
    """
    Prompts the user for input and validates it against the provided options.

    Args:
        prompt (str): The message to display to the user.
        valid_options (list): A list of valid options the user can enter.

    Returns:
        str: The user's input if valid, otherwise prompts again.
    """
    while True:
        user_input = input(prompt)
        if user_input.lower() in valid_options:
            return user_input.lower()
        else:
            print(f"Invalid input. Please choose from: {', '.join(valid_options)}")

def get_desired_length():
    """
    Prompts the user for desired password length and validates it to be a positive integer.
    Returns:
        int: The user-specified password length.
    """
    while True:
        try:
            length = int(input("Enter desired password length (minimum 8 characters): "))
            if length >= 8:
                return length
            else:
                print("Password length must be at least 8 characters. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def include_uppercase():
    """
    Prompts the user to include uppercase letters in the password.
    Returns:
        bool: True if user wants uppercase letters, False otherwise.
    """
    return get_user_choice("Include uppercase letters (y/n): ", ["y", "n"]) == "y"

def include_numbers():
    """
    Prompts the user to include digits in the password.
    Returns:
        bool: True if user wants digits, False otherwise.
    """
    return get_user_choice("Include numbers (y/n): ", ["y", "n"]) == "y"

def include_special_chars():
    """
    Prompts the user to include symbols in the password.
    Returns:
        bool: True if user wants symbols, False otherwise.
    """
    return get_user_choice("Include special characters (y/n): ", ["y", "n"]) == "y"

def generate_password(length, include_uppercase, include_numbers, include_special_chars):
    """
    Generates a random password based on user-defined criteria.
    Args:
        length (int): The desired length of the password.
        include_uppercase (bool): Whether to include uppercase letters.
        include_numbers (bool): Whether to include digits.
        include_special_chars (bool): Whether to include symbols.

    Returns:
        str: The generated password.
    """

    # Start with an empty character set
    char_set = ""
    
    # Add uppercase letters if the user wants them
    if include_uppercase:
        char_set += uppercase_chars
    
    # Add digits if the user wants them
    if include_numbers:
        char_set += digits
    
    # Add special characters if the user wants them
    if include_special_chars:
        char_set += symbols
    
    # Always include lowercase letters
    char_set += lowercase_chars

    # Ensure that at least one character type is chosen
    if not char_set:
        raise ValueError("Password must include at least one character type (uppercase letters, lowercase letters, numbers, or special characters).")

    # Generate a random password of the specified length using the selected character set
    password = "".join(random.sample(char_set, length))
    return password

# Start the process of generating a password

# Get the desired password length from the user
desired_length = get_desired_length()

# Ask the user if they want uppercase letters in their password
include_upper = include_uppercase()

# Ask the user if they want digits in their password
include_num = include_numbers()

# Ask the user if they want special characters in their password
include_special = include_special_chars()

# Generate the password using the user preferences
generated_password = generate_password(desired_length, include_upper, include_num, include_special)

# Display the generated password
print(f"Your generated password is: {generated_password}")
