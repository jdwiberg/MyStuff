from cs50 import SQL
import csv


def create_tables():
    db = SQL('sqlite:///roster.db')
    houses = []
    with open('students.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        db.execute('DELETE FROM students;')
        db.execute('DELETE FROM houses;')
        db.execute('DELETE FROM relationships;')
        for row in reader:
            name = row['student_name']
            house = row['house']
            head = row['head']
            db.execute('INSERT INTO students (student_name) VALUES (?)', name)
            if house not in houses:
                houses.append(house)
                db.execute('INSERT INTO houses (house, head) VALUES (?,?)', house, head)
            db.execute("INSERT INTO relationships (house_id, student_id) VALUES ((SELECT id FROM houses WHERE (house = ?)), (SELECT id FROM students WHERE (student_name = ?)))", house, name)


create_tables()






