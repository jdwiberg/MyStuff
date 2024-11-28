import time

class Node:
     def __init__(self, name, price, stock, ref):
        self.name = name
        self.price = price
        self.stock = stock
        self.ref = ref


class LinkedList:
     # ---------------Create an empty linked list -------------

    def __init__(self):
        self.start_node = None

    # -------------Insert Item Into List --------------------

    def insert_item(self):
        name = input("Enter item name: ")
        parent = input(f"Which item should {name} follow?\n(enter 0 for beginning, -1 for end):  ")
        price = float(input("Enter new item's price: "))
        stock = get_int('Enter # of new items in stock: ')

        if parent == '0':
            if self.start_node != None:
                self.start_node = Node(name, price, stock, self.start_node)
            else:
                 self.start_node = Node(name, price, stock, None)
            print(f"{name.capitalize()} was added to the beginning of the list.")

        elif parent == '-1':
            if self.start_node != None:
                n = self.start_node
                while True:
                    if n.ref == None:
                        n.ref = Node(name, price, stock, None)
                        break
                    else:
                        n = n.ref
            else:
                self.start_node = Node(name, price, stock, self.start_node)
            print(name.capitalize(), "was added to the end of the list.")

        else:
            n = self.start_node
            while n is not None:
                if n.name == parent:
                    break
                n = n.ref
            if n is None:
                print("Item not in list")
                return
            else:
                addition = Node(name, price, stock, None)
                addition.ref = n.ref
                n.ref = addition

            print(f"Item {name} added at after {parent}.")


    # --------------- Traverse and Print the Linked List  ----------------------

    def traverse_list(self):
         print("Linked List: ", end = " ")
         if self.start_node is None:
             print("List is empty")
             return
         else:
             n = self.start_node
             while n is not None:
                 print(n.name, end =" " )
                 n = n.ref
         print(" ")


    # ------------- Find High Priced Items --------------------------
    def find_high_price(self, price):
        check = 0
        n = self.start_node
        while n != None:
            if n.price >= price:
                print(n.name, end=", ")
                check = 1
            n = n.ref
        if check != 1:
            print(f"No items above price: ${"{:.2f}".format(price)}.")


    # -------- Find Low Stock Items ----------------------
    def find_low_stock(self):
        check = 0
        n = self.start_node
        count = 20
        while n != None:
            if n.stock < count:
                print(n.name, end=", ")
                check = 1
            n = n.ref
        if check != 1:
            print("No low stock items")

#----------------------- Main Functions -----------------------------

def get_int(input_statement):
    while True:
        try:
            number = int(input(input_statement))
            return number
        except ValueError:
            print('Please enter an integer.')

def get_float(input_statement):
    while True:
        try:
            number = float(input(input_statement))
            return number
        except ValueError:
            print('Please enter a decimal number.')

def main():
    My_List = LinkedList()

    choice = 0
    while choice != 5:
        time.sleep(1)
        print("\nGrocer, what do you want to do?\n")
        print("1 = Insert an item ")
        print("2 = Traverse and Display List ")
        print("3 = Find Products Above Price __ ")
        print("4 = Find Low Stock Products")
        print("5 = Exit")
        choice = get_int("\nEnter Choice: ")

        time.sleep(1)

        if choice == 1:
            My_List.insert_item()
        elif choice == 2:
            My_List.traverse_list()
        elif choice == 3:
            price = get_float("Enter specified price floor: ")
            My_List.find_high_price(price)
        elif choice == 4:
            My_List.find_low_stock()
        else:
            print("\nPlease choose an option listed aboove (1-5)\n")





    print("\nGoodbye\n")


main()
