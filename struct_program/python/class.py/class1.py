def main():
    p = 1
    pt = 0
    st = 0
    dt = 0
    same = input("Did everyone have the same meal? ")
    same = same.lower()
    if 'y' in same and same.count(" ") == 0:
        pt = int(input(f'How many pizzas did each person eat? '))
        st = int(input(f'How many soft drinks did each person drink? '))
        dt = int(input(f'How many desserts did each person have? '))
    elif 'n' in same and same.count(" ") == 0:
        party = int(input('How many people ate today? '))
        for i in range(party):
            pizzas = int(input(f'How many pizzas did person {p} eat? '))
            pt += pizzas
            sodas = int(input(f'How many sodas did person {p} drink? '))
            st += sodas
            desserts = int(input(f'How may desserts did person {p} have? '))
            dt += desserts
    else:
        print('Please answer using yes or no.')
        main()
    ip = 10
    sd = 2
    dess = 5
    check = round((ip * pt) + (sd * st) + (dess * dt), 2)
    print(f'Meal: ${check}')
    tax = round(check * 0.07, 2)
    print(f'Tax: ${tax}')
    tip = round((check + tax) * .18, 2)
    print(f'Tip: ${tip}')
    total_bill = round(check + tax + tip, 2)
    print(f'Total Bill: ${total_bill}')
main()
