

def main():
    n =  get_int("How many sets of data will there be? ")

    for i in range(n):
        set = input("Enter the data set number, the capacity, and the weight of ten potatoes: ").split()
        if len(set) != 12:
            print("Input Error")
            break
        total = 0
        for p in range(len(set)):
            try:
                set[p] = int(set[p])
            except:
                print("Input Error")
                break
        for p in range(2, 12):
            total += set[p]

        if total >= set[1]:
            print(f'{set[0]} YES')
        else:
            print(f'{set[0]} NO')


def get_int(input_statement):
    while True:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            print('Please enter an integer.')
main()
