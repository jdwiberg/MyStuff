
def main():
    num = int(input("Enter the number: "))
    if num < 5550000:
        print('no')
        return
    num = num % 5550000
    if num >= 0 and num <= 9999:
        print("yes")
    else:
        print("no")
main()

