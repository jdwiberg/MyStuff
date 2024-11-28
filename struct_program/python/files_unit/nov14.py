from sys import argv

# def main():
#     try:
#         global writer
#         global reader
#         writer = open(argv[2], 'a')
#         reader = open(argv[1], 'r')
#     except:
#         print('File Likely Not Found. Usage: python program reader writer')

#     for line in reader:
#         line = line.rstrip()
#         if line.endswith('1998') and not line.startswith('x-mailer'):
#             writer.write(line + '\n')

def second():
    with open('new_file.txt', 'w') as writer:
        with open('mbox1.txt', 'r') as reader:
            for line in reader:
                line = line.rstrip()
                if line.endswith('1998') and not line.startswith('From'):
                    writer.write(line + '\n')

# main()
second()
