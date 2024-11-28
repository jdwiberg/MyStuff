

def create_list():
    with open('randomtext.txt', 'r') as file:
        reader = file.read()
        reader = reader.split()
        words = []
        for word in reader:
            if word not in words:
                words.append(word)
        words.sort()
        return words


def lengths():
    with open('mbox1.txt', 'r') as reader:
        lens = []
        for line in reader:
            if line.startswith('Content-Length'):
                line = line.split()
                lens.append(int(line[1]))

        lens.sort()
        avg = sum(lens) / len(lens)
        avg = round(avg, 2)
        print(f"MESSAGE LENGTHS - Shortest: {lens[0]}, Longest: {lens[-1]}, Average: {avg}")

# print(create_list())
lengths()
