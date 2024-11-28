# training from https://www.w3schools.com/python/python_strings_slicing.asp
a = "banana's are awesome"
# ask if a string is in a string
print('are' in a)
# print the fifth char in the string
print(a[4])
# iterate over the string
for a in "bananas":
    print(a)
# print the length of a string
a = "banana's are awesome"
print(len(a))
# Check for words in a string
if "are" in a:
    print(f'The word "are" is in "{a}"')
if "poo" not in a:
    print(f'The word "poo" is not in "{a}"')
# print from or up to a certain part of a string
print(a[5:])
print(a[:5])
# Print from the end of a string
b = 'get this string from the end'
print(b[5:])
# print in upper/lower case
print(a[1].upper())
print(a.lower())
# remove whitespace
b = '    hello world       '
print(b.strip())
b = 'xello'
# replace string
print(b.replace('x', 'h'))
# split string
b = 'hello'
print(b.split("e"))
# capitalize string
text = input('Name? ')
text.capitalize()
print(text)
