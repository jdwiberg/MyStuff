# TODO
from cs50 import get_string

def main():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    punctuation = ['.', '?', '!']
    # get some text
    reader = get_string('Please enter your text here: ')
    reader = reader.lower()

    # count spaces (this is words - 1)
    space_count = 0
    for i in range(len(reader)):
        if reader[i] == " ":
            space_count += 1
    word_count = space_count + 1

    # find your word multiplier
    word_mult = word_count / 100

    # find how many letter there are
    letter_count = 0
    for i in range(len(reader)):
        if reader[i] in alphabet:
            letter_count += 1
    letters_per_hundredw = letter_count / word_mult

# find how many punctuation marks there are
    # divide this by WORDMULT to find sentences per 100 words
    sent_count = 0
    for i in range(len(reader)):
        if reader[i] in punctuation:
            sent_count += 1
    sent_per_hundredw = sent_count / word_mult

# find the level by using algorithm 0.0588 * L - 0.296 * S - 15.8
    level = letters_per_hundredw * 0.0588 - 0.296 * sent_per_hundredw - 15.8
    if level > 16:
        print('Grade 16+')
    elif level < 1:
        print('Before Grade 1')
    else:
        print(f'Grade {round(level)}')

main()
