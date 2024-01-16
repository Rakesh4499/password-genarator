import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user input for password length
try:
    password_length = int(input("Enter the desired length of the password: "))
except ValueError:
    print("Please enter a valid integer for password length.")
    exit()

# Check if the password length is greater than 0
if password_length <= 0:
    print("Password length must be greater than 0.")
    exit()

# Generate and display the password
password = generate_password(password_length)
print(f"Generated Password: {password}")
