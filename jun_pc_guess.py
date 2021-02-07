import random
def computer_guess(x):
    low = 1
    high = x
    feedback=''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high
        feedback = input(f'is {guess} too high (H) too low (L) correct(C)?? ').lower()
        if feedback =='h' :
            high = guess - 1
        elif feedback =='l':
            low = guess + 1
    print(f'yay, the computer guess the number , {guess} , correctly! ')
        
computer_guess(1000)