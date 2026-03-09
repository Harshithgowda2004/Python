import random

def play():
    number = random.randint(1,100)
    attempts = 0

    while True:
        guess = int(input("Guess number (1-100): "))
        attempts += 1

        if guess < number:
            print("Too Low")
        elif guess > number:
            print("Too High")
        else:
            print("Correct! Attempts:", attempts)
            return 10