# Jake Wiberg CS-113 Homework week 9
import time


class Student:
    def __init__(self, id, name):
        self.name = name
        self.id = int(id)

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for i in range(size)]

    def hash(self, key):
        return (int(key) % self.size)

    def insert_student(self, student):
        index = self.hash(student.id)
        self.table[index].append(student)

    def search(self, id):
        index = self.hash(id)
        for pupil in self.table[index]:
            if id == pupil.id:
                return pupil.name
        return None

    def scan(self):
        for spot in self.table:
            if len(spot) != 0:
                for pupil in spot:
                    print(f"{pupil.id}: {pupil.name}")

    def student_remove(self, id):
        index = self.hash(id)
        for pupil in self.table[index]:
            if pupil.id == id:
                self.table[index].remove(id)




def get_int(input_statement):
    while True:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            print('Please enter an integer.')



def main():
    table = HashTable(20003)
    while True:
        print("----------------------------------------------")
        print("Enter 1 to Add a new student")
        print("Enter 2 to Print out the database")
        print("Enter 3 to Find a student using their number")
        print("Enter 4 to Delete a student's record")
        print("Enter 5 to Exit", end='\n\n')
        time.sleep(1)
        choice = input("What is your choice: ")


        if choice == '1':
            id = get_int("\nEnter student's ID: ")
            name = input("\nEnter student's name: ")
            student = Student(id, name)
            table.insert_student(student)
            print(f"{name} ({id}) has been added.")
        elif choice == '2':
            table.scan()
        elif choice == '3':
            id = input("\nEnter student's ID: ")
            print(table.search(id))
        elif choice == '4':
            id = input("\nEnter student's id: ")
            table.student_remove(id)
        elif choice == '5':
            print("\n\nGoodbye")
            break
        else:
            print("Enter a number 1-5")

main()


