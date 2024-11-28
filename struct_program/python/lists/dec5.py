

def first():
    old_list = [1,2,3,3,3,4,4,5,6,6,6,6,7,7,8,8,8,9,10,11,11,11,11,12,13,13,14,15,15,15]
    new_list = []
    for num in old_list:
        if num not in new_list:
            new_list.append(num)
        else:
            continue
    return new_list




print(first())

