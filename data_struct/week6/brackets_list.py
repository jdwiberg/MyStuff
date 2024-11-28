


def main(string):
    stack = []

    for char in string:
        if char == '(':
            stack.append('p')
        elif char == ')':
            if stack[-1] != 'p':
                return False
            try:
                stack.pop(-1)
            except:
                return False

        elif char == '[':
            stack.append('b')
        elif char == ']':
            if stack[-1] != 'b':
                return False
            try:
                stack.pop(-1)
            except:
                return False

        elif char == '{':
            stack.append('a')
        elif char == '}':
            if stack[-1] != 'a':
                return False
            try:
                stack.pop(-1)
            except:
                return False
    if len(stack) == 0:
        return True

string =  input("Input a string that uses (), [], and {}.\n")
if main(string):
    print('This format is correct')
else:
    print('This format is not correct')



