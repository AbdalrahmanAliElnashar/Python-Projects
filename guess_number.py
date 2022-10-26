# a program that make a computer choice a random number and you try to guess it

import random # lib to create random numbers


def guess(x):
    
    random_number = random.randint(1, x) # create random integers numbers from 1 to n or x
    my_guess = 0
    
    # we will use while loop to still work untill the guess number is not correct
    while my_guess != random_number:
        my_guess = int(input(f'Guess a number between 1 and {x} : '))
        if my_guess > random_number:
            print("guess again, Too high !!")
        elif my_guess < random_number:
            print('guess again, Too low !!')

            
    print(f'Congrats, you guess the random number {random_number}, correctly')
    
guess(10)
