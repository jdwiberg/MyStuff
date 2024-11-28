
def main():
    text = input('Give text: ')
    print(length(text))

def length(string):
    counter = 0
    for i in string:
        counter += 1
    return counter

main()
