

hall = 300
mezzanine = 100

def main(hall, mezzanine):
    while True:
        if hall + mezzanine == 0:
            break
        while True:
            seat_type = input('Enter 1 for Hall and 2 for Mezzanine: ')
            if seat_type == '1':
                seat_type = hall
                adult_price = 10
                kid_price = 7
                break
            elif seat_type == '2':
                seat_type = mezzanine
                adult_price = 8
                kid_price = 5
                break

        adults = get_int('Number of adults: ')
        kids = get_int('Number of children: ')
        if seat_type < kids + adults:
            print('Not enough space in section. Please try again.')
            main(hall, mezzanine)
        if seat_type == hall:
            hall -= kids + adults
        elif seat_type == mezzanine:
            mezzanine -= kids + adults


        atotal = adult_price * adults
        ktotal = kid_price * kids
        total = ktotal + atotal

        print(f"Great, you got {adults} adult tickets for ${atotal} and {kids} kids tickets for ${ktotal} so your total is ${total}.", end='\n\n')
        print(f"Seats remaining: Hall {hall} Mezzanine {mezzanine}.", end='\n\n\n')


def get_int(input_statement):
    while True:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            continue

main(hall, mezzanine)



