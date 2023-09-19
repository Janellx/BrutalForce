import random
import time
import string

def crack(password):
    char_pool = ""
    attempts = 0

    for char in password:
        if char in string.ascii_letters:
            char_pool += string.ascii_letters
        if char in string.digits:
            char_pool += string.digits
        if char in string.punctuation:
            char_pool += string.punctuation

    while True:
        guess = ''.join(random.choice(char_pool) for _ in range(len(password)))
        print(">>>>", guess, "<<<<")
        attempts += 1
        if guess == password:
            return attempts


startTime = time.time()
password = input("Enter the password: ")
attempts = crack(password)
endTime = time.time()
elapsedTime = endTime - startTime

print(f"This took {elapsedTime} seconds to crack")
print(f"and took {attempts} attempts!")
