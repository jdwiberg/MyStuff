
def main():
    age = get_int('Please enter your age. ')
    base_sal = 0
    if age >= 18 and age <=30:
        base_sal = 1000
    elif age >= 31:
        base_sal = 1200

    edu = input("Please enter your education level (Note 'B' for Bachelor's, 'M' for Master's, 'P' for PhD")
    if edu.lower() == 'b':
        base_sal *= 1.1
    elif edu.lower() == 'm':
        base_sal *= 1.2
    elif edu.lower() == 'p':
        base_sal *= 1.3
    else:
        print('Please enter a valid educaiton level. (See notes for usage)')
        main()
        return 1

    exp = get_int("How many years of experience do you have? ")
    if exp > 10:
        base_sal *= 1.1

    print(f'Your base salary is ${"%.2f" % base_sal} per month.')

def get_int(input_statement):
    while True:
        try:
            n = int(input(input_statement))
            if n >= 0:
                return n
        except ValueError:
            print('Not an integer. Please try again.')

main()






