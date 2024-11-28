import sys

def finder():
    #  find() looks for a character or characters in a string
    #  gives us the starting position of the string in the string starting at 0
    #  if string not mound, will ouput -1

    word = 'congratulations'

    print(word.find('rat'))
    # outputs 4

    print(word.find('mouse'))
    # outputs -1

def stripper():
    # strip() takes out all of the whitespace

    word = '     hello world   '
    print(word.strip())
    # prints 'hello'

    # rstrip() and lstrip() do it from the left and right
    print(word.rstrip(), word.lstrip())

def counter():
    # count('x') will count all the x in a string
    string = 'Hello my name is Jake. I am a student a Sacred Heart.'
    print(string.count('a'))
    # prints 7

def replacement():
    # replace() take two argument. Replaces first with second in a string.
    string = 'how much wood could a woodchuck chuck if a woodchuck could chuck wood'
    print(string.replace('wood', 'fire'))

def main():
    

stripper()




