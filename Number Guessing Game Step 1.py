import random
secret_number = random.randint(1, 100)
attempts = 0
while attempts < 7:
    guess = int(input("Your guess: "))
    attempts += 1
    if guess == secret_number:
        print(f"Bravo! found in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")
    if guess != secret_number:
        print ("Lost! The secret number was", secret_number)
        

