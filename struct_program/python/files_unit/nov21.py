import sys

def main():
    # key_word = sys.argv[1]
    # # key_word = input('Insert Word for Counting: ')
    with open('mbox1.txt', 'r') as file:
        reader = file.read()
        reader = reader.split()
        counts = {}
        bigs = []
        for word in reader:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        #     if counts[word] > 4000 and word not in bigs:
        #         bigs.append(word)
        # print(bigs)
    counter = 0
    for word in sorted(counts, key=lambda word: counts[word], reverse=True):
        counter += 1
        print(f"'{word}' shows up {counts[word]} times")
        if counter > 2:
            break

main()
