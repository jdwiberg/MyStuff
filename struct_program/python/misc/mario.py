
def main():
    height = get_int('Height: ')
    spaces = height
    tags = 1

    for i in range(height):
        print(' ' * (spaces - 1), end="")
        print('#' * tags, end='')
        print('  ', end='')
        print('#' * tags)
        spaces -= 1
        tags += 1


def get_int(input_statement):
    while True:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            print('Please enter an integer.')

main()