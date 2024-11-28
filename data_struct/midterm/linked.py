import time


class Employee:
    def __init__(self, name, salary, dependants):
        self.name = name
        self.salary = salary
        self.dependants = dependants


def add_employee(employee_list):
    name = input("Enter the employee's name: ")
    salary = get_int("Enter the employee's salary (no commas): ")
    dependants = get_int("Enter the employee's number of dependants: ")

    employee_list.append(Employee(name, salary, dependants))

    print(f"{name} has been added to the employee database.")


def get_int(input_statement):
    while True:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            print('Please enter an integer.')


def main():
    employee_list = []

    choice = 0
    while True:
        time.sleep(1)
        print("\nWhat would you like to do?\n")
        print("1 = Add a new employee ")
        print("2 = Print Employee Information ")
        print("3 = Display number of employees ")
        print("4 = Print names of high salary employees (>100k) ")
        print("5 = Give employees with two or more dependants a '10%' raise ")
        print("6 = Display the total amount of the salaries the company pays ")
        print("7 = Exit")
        choice = get_int("\nEnter Choice: ")

        time.sleep(1)

        if choice == 1:
            add_employee(employee_list)
        elif choice == 2:
            for employee in employee_list:
                print(f"Name: {employee.name}, Salary: {employee.salary}, Dependants: {employee.dependants}")
        elif choice == 3:
            num = len(employee_list)
            print(f"There are {num} employees at this company.")
        elif choice == 4:
            print("The employees with a salary greater than 100k per year are: ")
            count = 0
            for employee in employee_list:
                if employee.salary > 100000:
                    print(f"{employee.name}: {employee.salary}")
                else:
                    count += 1
            if count == len(employee_list):
                print("None")
        elif choice == 5:
            count = 0
            for employee in employee_list:
                if employee.dependants >= 2:
                    employee.salary = round(employee.salary + (employee.salary * 0.1))
                    print(f"{employee.name}'s salary has been increased 10 percent from {round(employee.salary / 1.1)} to {employee.salary}.")
                else:
                    count += 1
            if count == len(employee_list):
                print("There are no employees with 2 or more dependants.")
        elif choice == 6:
            total = 0
            for employee in employee_list:
                total += employee.salary
            print(f"This compnay pays ${total} in salaries each year.")
        elif choice == 7:
            break
        else:
            print("\nPlease choose an option listed aboove (1-7)\n")

main()
print("Program terminated. Goodbye!")
