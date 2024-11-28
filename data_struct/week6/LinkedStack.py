class Node:
     def __init__(self, data):
         self.item = data
         self.ref = None

class Stack:
     # ---------------Create an empty linked list -------------
     
     def __init__(self):
         self.top = None
         
     # --------------- Traverse the linked list  ----------------------
     
     def traverse_list(self):
         print("Stack: ", end = " ")
         if self.top is None:
             print("Stack is empty")
             return
         else:
             n = self.top
             while n is not None:
                 print(n.item, end =" " )
                 n = n.ref
         print(" ")        
                 
    #  ------------- PUSH  ----------------------
    
     def Push(self, data):
            new_node = Node(data)
            new_node.ref = self.top
            self.top = new_node
           
   # -------------- Pop  ------------------

     def Pop(self):
            if self.top is None:
                print("Stack is empty!")
                return
            x = self.top.item  
            self.top = self.top.ref
            return x

# -------------------------Main-----------------        
My_Stack = Stack()

choice = 0
while choice != 4:
    print("\n Stack Demo, what do you want to do?")
    print(" 1 = Push ")
    print(" 2 = Pop ")
    print(" 3 = Print Stack")
    print(" 4 = Exit ")
    choice = int(input("\n Enter Choice: "))

    if choice==1:
        num = int(input("\n Enter number to push: "))
        My_Stack.Push(num)
        print( num , " pushed on stack")
    elif choice==2:
        x = My_Stack.Pop()
        print(x,  " was popped out")
    elif choice==3:
        My_Stack.traverse_list()
         
      
print("\n Goodbye \n")
