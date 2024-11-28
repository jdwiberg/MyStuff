

def main():
    while True:
        alphabet = ('abcdefghijklmnopqrstuvwxyz')
        string = input('What is your string? ')
        string = string.lower()
        for i in range(len(string)):
            if string[i] == 'y':
                string = string.replace(string[i], 'a', 1)
            elif string[i] == 'z':
                string = string.replace(string[i], 'b', 1)
            elif string[i] in alphabet:
                spot = int(alphabet.find(string[i]))
                spot_string = string.find(string[i])
                string = string.replace(string[spot_string], alphabet[spot + 2].upper(), 1)
        print(string.lower())
main()
