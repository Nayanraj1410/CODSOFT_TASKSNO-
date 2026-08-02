import string
import random

length = int(input("Enter the desired password length: "))
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for _ in range(length))

print("Generated Password:", password)
