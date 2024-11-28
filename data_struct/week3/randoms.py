import random
import array


def main():
    nums = array.array('i', [])
    append_randoms = lambda nums, n=5000: nums.extend(random.randint(0, 20001) for i in range(n))
    append_randoms(nums)

    sorted_nums = array.array('i', sorted(nums))

    while True:
        try:
            input_number = int(input('Enter an integer between 0 and 20,000: '))
            break
        except ValueError:
            pass

    if input_number > 20000:
        print('number must be less than 20,000')
        main()

    if linear_search(sorted_nums, input_number) == 1:
        print(f"{input_number} was found by linear search")
    else:
        print(f"{input_number} was not found by linear search")

    if binary_search(sorted_nums, input_number) == 1:
        print(f"{input_number} was found by binary search")
    else:
        print(f"{input_number} was not found by binary search")


def linear_search(nums, number):
    for num in nums:
        if num == number:
            return 1

    return -1


def binary_search(nums, number):
    f = len(nums) - 1
    b = 0
    while b <= f:
        a = (f + b) // 2
        if number == nums[a]:
            return 1
        if number < nums[a]:
            f = a - 1
        elif number > nums[a]:
            b = a + 1
    return -1


main()

