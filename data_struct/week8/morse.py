# Morse Code Palindromes, Week 8 Classwork
# Jacob Wiberg
# CS-112-D
import time

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def translate(sample):
    morse = []
    for char in sample:
        if char in MORSE_CODE_DICT:
             morse.append(MORSE_CODE_DICT[char])
        elif char.upper() in MORSE_CODE_DICT:
                morse.append(MORSE_CODE_DICT[char.upper()])
    morse = "".join(morse)

    return morse


def check(morse):
    morse_backward = morse[::-1]
    if len(morse) == 0:
         print("NO")
    elif morse_backward == morse:
         print("YES")
    else:
         print("NO")
print("This program checks for morse code palindromes.\nSymbols that are not a letter or number will be ignored.", end="\n\n")
time.sleep(1)

while True:
    sample = input("Enter a possible morse code palindrome: ")
    check(translate(sample))

