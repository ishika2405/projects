import random

def guess(x):
    random_num = random.randint(1, x)
    guess = None
    while guess != random_num:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < random_num:
                print("Too low")
            elif guess > random_num:
                print("Too high")
        except ValueError:
            print("Please enter a valid number!")

    print("Congratulations! You guessed it right.")

guess(10)
