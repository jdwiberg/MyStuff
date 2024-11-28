import csv

with open('names.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)

    with open('new_news.csv', 'w') as new_file:
        fieldnames = ['name', 'surname', 'email']
        writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')

        writer.writeheader()

        for line in reader:
            writer.writerow(line)