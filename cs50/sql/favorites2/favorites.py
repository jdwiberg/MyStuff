import csv
import sys
from cs50 import SQL

with open('favorites.csv', 'r') as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row['problem']
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1

for favorite in sorted(counts, key=lambda favorite: counts[favorite], reverse=True):
    print(f'{favorite}: {counts[favorite]}')

# favorite = input('Favorite: ')
# if favorite in counts:
#     print(f'{favorite}: {counts[favorite]}')
