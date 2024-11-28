
def main():
    while True:
        try:
            n = int(input("How many times would you like to agree? "))
            if n > 0:
                break
        except ValueError:
            print('Not an integer. Please try again.')
    agreement_statement(n)


def agreement_statement(n):
    for i in range(n):
        answer = input('Do you agree? ')

        if 'y' in answer.lower() and answer.count(" ") == 0:
            print('Agreed.')
        elif 'n' in answer.lower() and answer.count(" ") == 0:
            print('Not Agreed.')
        else:
            print('Please try again.')
            agreement_statement()

main()