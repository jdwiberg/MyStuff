from sys import argv
import time

def main():
    print(find_temp())
    if len(argv) == 4:
        find_largest(argv[1], argv[2], argv[3])
    else:
        print('Please enter 3 command line arguments if you want to compare some numbers!')
        time.sleep(3)
        a = input('Would you like to do it all again? ')
        if 'y' in a.lower():
            main()
        else:
            print('Okay, see you later!')

def find_largest(x, y, z):
    if x > y and x > z:
        print(f'{x} is the largest')
    elif y > x and y > z:
        print(f'{y} is the largest')
    elif z > y and z > x:
        print(f'{z} is the largest')
    else:
        print('There is a tie for the largest')
        if x == z:
            print(f'{x} is the same as {z}')
        elif y == z:
            print(f'{y} is the same as {z}')
        else:
            print(f'{y} is the same as {x}')

def find_temp():
    to = get_int('What temperature would you like to convert? ')
    m = input('Would you like to start in Fahrenheit or Celcius? ')
    if 'f' in m.lower():
        temp = (to - 32) * (5/9)
        final = str(round(temp, 2)) + ' degrees Celcius'
        return final
    if 'c' in m.lower():
        temp = to * (9/5) + 32
        final = str(round(temp, 2)) + ' degrees Fahrenheit'
        return final

def get_int(input_statement):
    while True:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            print('Please enter a valid number.')
main()
