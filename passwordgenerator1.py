import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        print("Password length should be at least 8 characters.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        length = input("Enter the desired length of the password (at least 8 characters): ")
        if length.isdigit() and int(length) >= 8:
            length = int(length)
            break
        else:
            print("Invalid input. Please enter a number of at least 8.")
    
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()