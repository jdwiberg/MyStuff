# Jacob Wiberg    CS-112    Midterm Exam 1    2/28/2024
from time import sleep


def main():
    choice = 0
    weights = []
    while choice != 6:
        sleep(1)
        choice = print_menu()

        if len(weights) == 0 and choice != 1:
            sleep(1)
            print('Not enough data')
            main()

        if choice == 1:
            sleep(1)
            weight = get_int('Enter weight: ')
            if weight > 0:
                weights.append(weight)
                print('\nYour weight has been logged.')
                sleep(1)
            else:
                print('Your weight was not logged')
                sleep(1)

        elif choice == 2:
            sleep(1)
            m = max(weights)
            print(f'\nHighest weight: {m} pounds')
            sleep(1)

        elif choice == 3:
            sleep(1)
            m = min(weights)
            print(f'\nLowest weight: {m} pounds')
            sleep(1)

        elif choice == 4:
            sleep(1)
            total = weights[0] - weights[-1]
            if total > 0:
                print(f'You have lost {total} pounds.')
            else:
                print(f'You have gained {total * -1} pounds.')
                sleep(1)

        elif choice == 5:
            progress_chart(weights)

    sleep(1)
    print('\nGoodbye!\n')


def print_menu():
    print('\nWelcome to weight tracker!\n')
    print('Select 1 to add a new weight')
    print('Select 2 to show the highest weight')
    print('Select 3 to show the lowest weight')
    print('Select 4 to show your total loss/gain in weight')
    print('Select 5 to print a progess chart', end='\n\n')
    print('Select 6 to exit')

    choice = 100
    while choice < 1 or choice > 6:
        choice = get_int("Enter your choice: ")

    return choice


def progress_chart(weights):
    print("\nWeek\tWeight\tDifference", end='\n----------------------------\n')

    for i in range(len(weights)):
        print(i, end='\t')
        print(weights[i], end='\t')
        if i != 0:
            total = weights[i] - weights[i-1]
            print(total)
        else:
            print('0')

    print('----------------------------')


def get_int(input_statement):
    number = 0
    while number < 1:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            print('Please enter a valid choice.')


main()
