import random
import string
import pyperclip

def password_generator(length: int = 10, charecter: bool = True, numbers: bool = True, punctuation: bool = True) -> str:
    password_set = ''
    if charecter:
        password_set += string.ascii_letters
    if numbers:
        password_set += string.digits
    if punctuation:
        password_set += string.punctuation
    
    if not password_set:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(password_set) for _ in range(length))
    return password

def get_user_input():
    length = input("Enter password length (default = 10): ")
    try:
        length = int(length) if length else 10
        if length <= 0:
            print("Password length must be a positive integer. Using default length of 10.")
            length = 10
    except ValueError:
        print("Invalid input. Using default length of 10.")
        length = 10

    k = '-' * 20
    print(f"{k}Press Enter to Agree{k}")
    use_letters = input("Include letters? (y/n): ").lower() in ('y', '')
    use_numbers = input("Include numbers? (y/n): ").lower() in ('y', '')
    use_symbols = input("Include symbols? (y/n): ").lower() in ('y', '')
    
    return length, use_letters, use_numbers, use_symbols

def generate_password_cli():
    while True:
        length, use_letters, use_numbers, use_symbols = get_user_input()
        try:
            password = password_generator(length, use_letters, use_numbers, use_symbols)
            print("Generated Password:", password)

            copy = input("Press Enter to Copy the Password (or any key to skip): ")
            if copy == '':
                pyperclip.copy(password)
                print("Password Copied Successfully!!")
                
            exit_prompt = input("Press 'e' to Exit or any other key to continue: ").lower()
            if exit_prompt == 'e':
                break
        except ValueError as e:
            print("Error:", e)
if __name__ == "__main__":
    generate_password_cli()
