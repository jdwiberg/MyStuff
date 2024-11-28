import sys


def random():
    reader = open('randomtext.txt', 'r')
    words = []
    reader = reader.read()
    reader = reader.split()
    for word in reader:
        if word not in words and word.startswith('A'):
            words.append(word)
    words.sort()
    print(words)

def resent():
    reader = open('mbox1.txt', 'r')
    writer = open('newfile.txt', 'w')
    for line in reader:
        if line.startswith('Resent-Date') and 'Mar' in line:
            writer.write(line)

def numbers():
    numbers = []
    for i in range(100, 1001):
        if i % 6 == 0 and i % 7 == 0:
            numbers.append(i)
    print(len(numbers))

def emails():
    list1 = ['brickbat@verizon.net', 'magusnet@att.net', 'cliffski@icloud.com', 'andrei@optonline.net']
    for email in list1:
        email = email.split('@')
        print(email[0])

sys.argv[1]

