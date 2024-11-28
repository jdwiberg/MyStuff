def main():
    x = get_int('What is your first number? ')
    y = get_int('What is your second number? ')
    op = input('Please enter an operator: ')
    if op == '+':
        print(numbers[0] + numbers[1])
    elif op == '-':
        print(x - y)
    elif op == '/':
        print(x / y)
    elif op == '*':
        print(x * y)
    else:
        print('Please enter a valid operator')
        main()

def get_int(input_statement):
    while True:
        try:
            n = int(input(input_statement))
            if n > 0:
                return n
        except ValueError:
            print('Not an integer. Please try again.')
main()
