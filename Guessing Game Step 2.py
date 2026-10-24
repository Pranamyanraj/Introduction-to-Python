import random

secret_number = random.randint(1, 100)
attempts = 0
while attempts < 7:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess == secret_number:
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")