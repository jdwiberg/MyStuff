def main():
    while True:
        try:
            num = int(input('Positive integer: '))
            if num > 0:
                break
        except ValueError:
            print(end="")

    print(f'{len(str(num))} digits')
    
main()