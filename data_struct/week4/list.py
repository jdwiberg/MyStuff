import random


def main():
    nums_list = []
    for i in range(10):
         num = nums_list.append(get_int("Input an integer: "))
    print('')
    print(nums_list, end='\n\n')

    print(f"Sum: {sum(nums_list)}, Min: {min(nums_list)}, Max: {max(nums_list)}, Length: {len(nums_list)}", end='\n\n')

    random.shuffle(nums_list)
    print("Shuffled:", nums_list, end='\n\n')

    print("Sorted:", sorted(nums_list), end='\n\n')

    new = []
    for num in nums_list:
        if num not in new:
            new.append(num)
    print("No repeats:", sorted(new), end='\n\n')


def get_int(input_statement):
        while True:
            num = int(input(input_statement))
            try:
                num / 1
                return num
            except ValueError:
                print('Please enter an integer')


main()


