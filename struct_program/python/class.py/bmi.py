def main():
    weight = get_int('Weight (in pounds): ')
    weight = weight * 0.4536
    height = get_int('Height (in inches): ')
    height = height * 0.0254

    BMI = weight / (height ** 2)
    print(f'Your BMI is: {round(BMI)}.')

    if BMI < 18.5:
        print('This weight is under the optimal weight for this height.')
    elif BMI > 25:
        print('This weight is over the optimal weight for this height.')
    else:
        print('This weight is optimal for this height.')


def get_int(input_statement):
    while True:
        try:
            n = int(input(input_statement))
            if n >= 0:
                return n
        except ValueError:
            print('Not an integer. Please try again.')
main()