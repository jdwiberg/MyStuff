# Write a function to calculate the sum of all numbers divisible by 5 between 1 and 1000 (a thousand).
# Both numbers are included. Invoke the function to put the result on the screen.

def find_sum():
    numbers = []
    for i in range(1, 1001):
        if i % 5 == 0:
            numbers.append(i)
    total = sum(numbers)
    print(total)

# find_sum()


# Write a program to slice out and print the extensions (like ca, net, com) from the
# following list of e-mail addresses.

def adresses():
    list1 = ['wmszeliga@yahoo.ca', 'osaru@verizon.net', 'wildixon@outlook.com', 'drhyde@gmail.com']
    for email in list1:
        dot = email.find('.')
        print(email[dot+1:])

# adresses()

# Write a program to create a file (newlist.txt).Find all the lines that start with
# ‘Content-Length:’ in mbox1.txt and put those lines into the newlist.txt file.

def content_length():
    with open('mbox1.txt', 'r') as reader:
        with open('newlist.txt', 'w') as writer:
            for line in reader:
                if line.startswith('Content-Length:'):
                    writer.write(line)

# content_length()

# Write a program to open the file randomtext.txt. Create an empty list and put each word from the
# file into the list if it is not a duplicate. When your list is complete,
# sort it in alphabetical order and print it.

def random():
    with open('randomtext.txt', 'r') as reader:
        new_list = []
        reader = reader.read()
        reader = reader.split()
        for word in reader:
            if word not in new_list:
                new_list.append(word)
        new_list.sort()
        print(new_list)

# random()

def find_word():
    user = input('Word: ')
    counter = 0
    with open('mbox1.txt', 'r') as reader:
        reader = reader.read()
        reader = reader.split()
        for word in reader:
            if word.lower() == user or word == user:
                counter += 1
        print(counter)


find_word()





