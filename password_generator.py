import random
import string
import argparse

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ''

    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("No characters available to generate password.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password(password):
    with open('passwordlist.txt', 'a') as file:
        file.write(password + '\n')

def main():
    parser = argparse.ArgumentParser(description='Generate a random password.')
    parser.add_argument('-l', '--length', type=int, default=12, help='Length of the password')
    parser.add_argument('--upper', action='store_true', help='Include uppercase letters')
    parser.add_argument('--lower', action='store_true', help='Include lowercase letters')
    parser.add_argument('--digits', action='store_true', help='Include digits')
    parser.add_argument('--symbols', action='store_true', help='Include symbols')

    args = parser.parse_args()

    #  auto-enable defaults if user selects nothing
    if not (args.upper or args.lower or args.digits or args.symbols):
        args.upper = True
        args.lower = True
        args.digits = True

    if args.length <= 0:
        raise ValueError("Password length must be greater than 0.")

    password = generate_password(
        args.length,
        args.upper,
        args.lower,
        args.digits,
        args.symbols
    )

    print(f"Generated Password: {password}")
    save_password(password)
    print("Password saved to passwordlist.txt.")

if __name__ == "__main__":
    main()
