import random

minimum = int(input("Enter minimum number: "))
maximum = int(input("Enter maximum number: "))

secret_number = random.randint(minimum, maximum)

while True:
    guess = int(input("Guess the number: "))

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Correct! You guessed the number.")
        break
    