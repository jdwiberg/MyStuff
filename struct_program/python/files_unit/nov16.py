import sys

def name_finder():
    portal = open('mbox1.txt', 'r')
    sender_names = []
    for line in portal:
        if line.startswith('From: '):
            words = line.split('<')
            sender = words[0]
            name = sender[6:].rstrip()
            if name not in sender_names:
                sender_names.append(name)
    for i in range(len(sender_names)):
        print(sender_names[i], end=', ')


def new_email():
    old = 'brady2@apple.com'
    new = 'bradynew@apple.com'
    with open('mbox1.txt', 'r') as reader:
        file = reader.read()
        file = file.replace(old, new)
    writer = open('mbox1.txt', 'w')
    writer.write(file)

def copy_file():
    file = open(sys.argv[1], 'r')
    file = file.read()
    copy_file = open(f'CPY{sys.argv[1]}', 'w')
    copy_file.write(file)

def counter():
    file = sys.argv[1]
    file = open(file, 'r')
    file = file.read()
    words = file.split()
    length = len(words)
    print(length)





# name_finder()
# new_email()
# copy_file()
# counter()
