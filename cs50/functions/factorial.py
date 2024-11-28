import sys

def factorial(original_number):
    xx = original_number
    # multiply the original number by the number one lower until you are multiplying by 1
    for counter in range(original_number - 2):
        multiplier = original_number - counter - 1
        xx *= multiplier
    return xx
#  Get factorial starter from user
try:
    p = int(input('What do you want to find the factorial of? ' ))
    print(factorial(p))
except ValueError:
    sys.exit('Please use integers only. Reminder: this is factorial function not gamma function.')

# # Do it yourself
# for i in range(15, 2, -1):
#     print(factorial(i))

