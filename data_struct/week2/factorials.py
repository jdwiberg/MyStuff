import math


def main():
    number = -1
    while number < 0:
        try:
            number = int(input('Give a positive integer: '))
        except ValueError:
            main()

    print(FactRecursion(number))
    print(FactIterate(number))


def FactRecursion(i):
    if i == 0:
        return 1
    else:
        return i * FactRecursion(i - 1)


def FactIterate(i):
    f = 1
    for n in range(2, i + 1, 1):
        f = f * n
    return f


main()
