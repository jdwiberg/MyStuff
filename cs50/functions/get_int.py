import time

def main():
    functions = (say_hello, say_bye)
    for i in range(2):
        functions[i]()
        time.sleep(1)
    global first_number
    first_number = get_int('What is your number? ')
    print(first_number)
    print(get_second_number('What is your second number? '))


def get_second_number(input_statement):
    second_number = get_int(input_statement)
    if second_number == first_number:
        print('Give me a different number')
        get_second_number(input_statement)
    else:
        return second_number



def get_int(input_statement):
    while True:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            print('Please enter an integer.')

def say_hello():
    print('Hello!')

def say_bye():
    print('Goodbye')


main()




