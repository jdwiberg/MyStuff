
def main():
    reader = open('mbox1.txt', 'r')
    writer = open('mbox1_writer.txt', 'w')
    for line in reader:
        line = line.rstrip()
        if line.endswith('1998'):
            print(line)


main()
