

n = int(input('How many eggs? '))
dozen = n // 12
loose = n % 12
total = (dozen * 3.25) + (loose * .45)

print(f"You ordered {n} eggs. That is {dozen} dozen eggs at $3.25 per dozen",
    f"and {loose} loose eggs at 45 cents each for a total of ${total}.")



