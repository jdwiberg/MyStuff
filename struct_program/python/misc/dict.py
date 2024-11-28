people = {
    "Carter": "45",
    "Jake": "97"
}

name = input('Name: ')
if name in people:
    print(f'Number: {people[name]}')
people["Gino"] = 69
print(people["Gino"])









# def check(word):
#     if word.lower() in words:
#         return True
#     else:
#         return False

# def load(dicitonary):
#     file = open(dictionary, "r")
#     for line in file:
#         word = line.rstrip()
#         words.add(word)
#     close(file)
#     return True

# def size():
#     return len(words)

# def unload():
#     return True
