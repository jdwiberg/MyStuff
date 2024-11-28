def main():

    dest = get_dest('Flight destination: ')
    nights = get_int('Nights stayed: ')
    rcdays = get_int('Total rental car days: ')

    print('')

    print(f'Flight Cost: ${fcost(dest)}')
    print(f'Hotel Cost: ${hcost(nights)}')
    print(f'Car cost: ${ccost(rcdays)}')

    print('')

    print(f'Total Cost: ${hcost(nights) + fcost(dest.lower()) + ccost(rcdays)}\n')

def hcost(n):
    hotel_cost = n * 150
    return hotel_cost

def fcost(d):
    try:
        if d == 'raleigh':
            flight_cost = 150
        elif d == 'miami':
            flight_cost = 200
        elif d == 'austin':
            flight_cost = 250
        elif d == 'san diego':
            flight_cost = 250
        return flight_cost
    except:
        print('Not a valid location. Please try again.')
        main()


def ccost(t):
    r = 50
    car_cost = r * t
    if t >= 7:
        car_cost -= 50
    elif t >= 3:
        car_cost -= 30
    return car_cost

def get_int(input_statement):
    while True:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            print('Please enter an integer.')

def get_dest(input_statement):
    acceptable_destinations = ('austin', 'miami', 'raleigh', 'san diego')
    while True:
        dest = input(input_statement)
        if dest.lower() in acceptable_destinations:
            return dest
        else:
            print('Please enter a supported destination.')
main()
