

def main():
    with open('mbox1.txt', 'r') as reader:
        with open('lines.txt', 'w') as writer:
            for line in reader:
                if line.startswith('Lines: '):
                    number = int(line[7:-1])
                    if number >= 100:
                        writer.write(line)
                        writer.write('')


main()

