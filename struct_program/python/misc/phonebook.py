import csv

with open("phonebook.csv", "a"):

    name = input('What is your name? ')
    number = input('What is your number? ')

    writer = csv.DictWriter('phonebook.csv', fieldnames=["name", "number"])
    writer.writerow({"name": name, "number": number})