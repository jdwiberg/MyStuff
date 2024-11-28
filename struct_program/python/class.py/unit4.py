
def main():
    op = input('What operation would you like to perfrom? ')
    fn = get_int('First number: ')
    sn = get_int('Second number: ')
    op = op.lower()

    if op == '+' or op == 'addition':
        print(add(fn, sn))
    elif op == '-' or op == 'subtraction':
        print(sub(fn, sn))
    elif op == '/' or op == 'division':
        print(round(div(fn, sn), 2))
    elif op == '*' or op == 'multiplication':
        print(mult(fn, sn))
    else:
        print('Improper usage. Please try again.')
        main()


def add(x, y):
    f = x + y
    return f

def sub(x, y):
    f = x - y
    return f

def mult(x, y):
    f = x * y
    return f

def div(x, y):
    f = x / y
    return f

def get_int(input_statement):
    while True:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            print('Please enter an integer.')
main()

