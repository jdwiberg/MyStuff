
def main():
    fruits_price = {
        "Bananas": 1.50,
        "Apples": 2.30,
        "Oranges": 4.50,
        "Cherries": 6.00
    }

    fruits_stock = {
        "Bananas": 35,
        "Apples": 42,
        "Oranges": 40,
        "Cherries": 12
    }
    print_table(fruits_price, fruits_stock)


def print_table(prices, stock):
    print('')
    print("Fruit\t\tPrice\tStock", end="\n-------------------------------\n")
    for key in prices:
        if len(key) < 8:
            print(f"{key}\t\t${"{:.2f}".format(prices[key])}\t{stock[key]}")

        elif len(key) >= 8:
            print(f"{key}\t${"{:.2f}".format(prices[key])}\t{stock[key]}")
    print('')


def value(fruits):
    total = []
    for key in  fruits

main()
