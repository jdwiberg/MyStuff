def one():
    num = [0,2,4,6,8,10,12,14,16,18,20]
    num2 = [1,3,5,7,9,11,13,15,17,19]
    num.extend(num2)
    num.sort()
    print(num)
    for i in range(4):
        num.remove(i)
    print(num)

def two():
    x = 5
    def add(y):
        y = y + 5
        return y
    print(add(x))
    print(x)

def three():
    # pop takes out the last element without arguments
    list = [1,2,3,4,5,6,7]
    print(list)
    list.pop()
    print(list)
    # pop takes index positions
    list.append(7)
    list.pop(0)
    print(list)

def four():
    listone = ['Jake', 'John', 'Lori', 'Sam']
    listtwo = ['Gus', 'Sug']
    listone.extend(listtwo)
    print(listone)

def five():
    # delete or del gets rid of indexes in lists (can be more than 1 spot)
    list = []
    for i in range(10):
        list.append(i)
    print(list)
    del list[2:6]
    print(list)

def avg(x):
    try:
        ave = sum(x) / len(x)
        return ave
    except TypeError:
        return "Input to 'avg' function must be a list."


def sumn():
    k


# one()
# two()
# three()
# four()
# five()

list = [3,2,4,5,3,5,6,7,7,10]
print(avg(list))
