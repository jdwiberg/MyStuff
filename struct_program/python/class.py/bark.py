from cs50 import get_int

def main():
    q = get_int('How many containers did you purchase? ')
    price = 10

    if q > 50:
        dprice = price - 0.1 * price
        oq = 50
    elif q > 100:
        dprice = price - 0.2 * price
        oq = 100
    else:
        dprice = price
        oq = 0

    total = price * (oq) + dprice * (q - oq)
    total_saved = (q * price) - (total)
    print(f'Your total is {"%.2f" % total}')
    if dprice != price:
        print(f'You saved ${"%.2f" % total_saved}!')

main()
