
Stack = []

choice = 0
while choice !=  5 :
    print("\nWhat do you want to do?")
    print(" 1. Push an item on the stack")
    print(" 2. Pop an item from stack")
    print(" 3. Print out stack")
    print(" 4. Display length of stack")
    print(" 5. Exit")
    choice = int(input(" Choice: "))
    if choice == 1 :
        x = int(input("\n Enter data to push: "))
        Stack.append(x)
        print( x , "added to Stack")
    elif choice == 2 :
        if len(Stack)>0 :
            y = Stack.pop()
            print("\n", y , " was popped")
        else:
            print("\n Stack is empty")
    elif choice == 3 :
         print("\nStack" , Stack)
    elif choice == 4 :
         print("\nStack size is ",len(Stack)) 
                 
print("Goodbye")
