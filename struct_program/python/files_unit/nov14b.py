

def definitions():
    # split method splits strings (the default splitter char is any whitespace but any character can be added as an argument)
    name = 'Jake Wiberg'
    split = name.split()
    print(split)
        # prints both names

    split_i = name.split('i')
    print(split_i)
        #  important: this does not print the 'i'


    # partition method splits a string into 3 tuples
        # these tuples are the parts before and after the char as well as the char
    email = 'wibergj@mail.sacredheart.edu'
    partition = email.partition('@')
    print(partition)

def pset():
    reader = open('mbox1.txt')
    for line in reader:
        if line.startswith('From: '):
            splitter = line.split()
            print(splitter[1], splitter[2])


pset()
# definitions()
