
def main():
    fruits = {
        "prices": {
            "Bananas": 1.50,
            "Apples": 2.30,
            "Oranges": 4.50,
            "Cherries": 6.00
        },

        "stock": {
            "Bananas": 35,
            "Apples": 42,
            "Oranges": 40,
            "Cherries": 12
        }
    }

    print_table(fruits)
    value(fruits)


def print_table(fruits):
    print('')
    print("Fruit\t\tPrice\tStock", end="\n-------------------------------\n")
    for key in fruits["prices"]:
        if len(key) < 8:
            print(f"{key}\t\t${"{:.2f}".format(fruits["prices"][key])}\t{fruits["stock"][key]}")

        elif len(key) >= 8:
            print(f"{key}\t${"{:.2f}".format(fruits["prices"][key])}\t{fruits["stock"][key]}")
    print('')


def value(fruits):
    summer = []
    for key in fruits["prices"]:
        total = fruits["prices"][key] * fruits["stock"][key]
        print(f"There are ${"{:.2f}".format(total)} of {key.lower()}.")
        summer.append(total)

    print(f"\nThe total value of the store is ${"{:.2f}".format(sum(summer))}.", end='\n\n')



main()
