# TODO
from cs50 import get_string, get_int
def main():
    while True:
        number = get_int("Number: ")
        if number < 0:
            print("The number must be an integer!")
        else:
            break


    last = 0
    digits = 0
    sumodds = 0
    sumevens = 0


    while number > 0:
        digits += 1

        sec_last = last

        last = number % 10

        if digits % 2 == 0:
            multiplier = last * 2

            if multiplier >= 10:
                n1 = multiplier // 10
                n2 = multiplier % 10
                multiplier = n1 + n2

            sumevens += multiplier
        else:
            sumodds += last

        number = number // 10

    firsts = (last * 10) + sec_last
    total_sum = sumevens + sumodds

    if total_sum % 10 == 0:
        if (digits == 13 or digits == 16) and last == 4:
            print("VISA")
        elif digits == 15 and (firsts == 34 or firsts == 37):
            print("AMEX")
        elif digits == 16 and (firsts >= 51 and firsts <= 55):
            print("MASTERCARD")
        else:
            print("INVALID")
    else:
        print("INVALID")
main()
