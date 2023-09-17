import random
import time
import string

startTime = time.time()

password = input ("Enter the password: ")


def crack(password):
    attempts=0
    while True:
        guess = ''.join(random.choices(string.ascii_letters + string.digits, k = len(password)))
        print(">>>>", guess, "<<<<")
        attempts +=1
        if guess == password:
            return attempts




endTime = time.time()
elapsedTime = endTime - startTime
attempts = crack(password)
print(f"This took {elapsedTime} seconds to crack")
print(f"and took {attempts} attempts!")