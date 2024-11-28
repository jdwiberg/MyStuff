# Convert Temperatures Table
# Jacob Wiberg

def main():
    print('')
    table(50, 100, 5)
    print('')


def table(s, e, n):
    # create the top of the table
    print("=" * 25)
    print("Fahrenheit", end='   ')
    print("Celcius", end='\n')
    print('-' * 25)


    # create body of the table
    for i in range(s, e + 1, n):
        print(i, end=' ' * (13 - len(str(i))))
        print(TempConvert(i))

    # create the bottom of the table
    print('=' * 25)


def TempConvert(fahr):
    celcius =  (5.0/9.0) * (fahr - 32.00)
    celcius = round(celcius)
    return celcius


main()
