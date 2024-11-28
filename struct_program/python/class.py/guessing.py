import random
import sys

def main():
# If you want to use command line arguments:
    if len(sys.argv) != 3:
        sys.exit("Usage: python guessing.py 'lower limit' 'upper limit")
    low = int(sys.argv[1])
    high = int(sys.argv[2])

# If you want to ask the user for input
    # low = get_int('Please specifiy the lower limit of the range. ')
    # high = get_int('Please specifiy the upper limit of the range. ')

    number = random.randint(low, high)
    guess = 0
    print(f'I am thinking of a number between {low} and {high}.\nYou have ten chances to guess it.')
    for guesses in range(10):
        guess = get_int('What is your guess? ')
        if guess > number:
            if guesses == 8:
                print('Last guess!')
            else:
                print('Too big')
        elif guess < number:
            if guesses == 8:
                print('Last guess!')
            else:
                print('Too small')
        else:
            print(f'You got it! The number was {number}!')
            print(f'You finished with {9 - guesses} guesses remaining!')
            break
        if guesses == 9:
            print(f'You ran out of guesses. My number was {number}.')

def get_int(input_statement):
    while True:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            print('Please enter an integer.')
main()
