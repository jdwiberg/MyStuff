
def main():
    salary = get_int('What is your salary? ')
    service = get_int('How many years have you served? ')
    if service <= 5:
        salary = salary * 1.03
    elif service >= 6 and service <= 10:
        salary = salary * 1.05
    else:
        salary = salary * 1.1
    print(f'Your salary is: ${"%.2f" % salary}.')

def get_int(n):
        while True:
            try:
                n = int(input(n))
                if n > 0:
                    break
            except ValueError:
                print('Not an integer. Please try again.')
main()