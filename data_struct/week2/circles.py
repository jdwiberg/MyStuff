import math


def main():
    r = input('Give a radius: ')
    try:
        r = int(r)
    except ValueError:
        main()

    make_table(r)


def area(r):
    a = math.pi * (r**2)
    return a


def circumference(r):
    c = 2 * math.pi * r
    return c


def make_table(r):
    print('=' * 30, end='')
    print('')
    print('Radius', end='\t')
    print('Area', end='\t')
    print('Circumference')
    print('-' * 30, end='')
    print('')

    for i in range(1, r + 1, 1):
        print(i, end='\t')
        print(round(area(i), 2), end='\t\t')
        print(round(circumference(i), 1))

    print('=' * 30, end='')
    print('\n')


main()
