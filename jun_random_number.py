# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# import random 

import random

def abcd(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number: 
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess<random_number:
                print(f'too small ')
            if guess>random_number:
                print(f'too big ')
        except:
            print('wrong input')
            guess = 0
    print(f'you found it {random_number}')

# def no_one():
#     print('hello there is no parameter')
# no_one()

abcd(10)



     
