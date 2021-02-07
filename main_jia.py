import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a random number between 1 and {x}:'))
        if guess < random_number:
            print('bigger.')
        elif guess > random_number:
            print('smaller')

    print(f'congrats, you guessed the number {random_number}')        

guess (10)