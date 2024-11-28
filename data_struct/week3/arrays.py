# Jacob Wiberg
# CS-112-D
import array


def array_practice():

    values = array.array('i', [])
    for i in range(10):
        try:
            x = int(input('Integer: '))
            values.append(x)
        except ValueError:
            print('Inputs must be single integers.')
            array_practice()

    total = sum(values)
    average = total / len(values)

    print(f"Sum: {total}, Avg: {average}")
    print("Greater than the average:", end=' ')
    for i in values:
        if i > average:
            print(f"'{i}'", end=' ')
    print('')

    print(f"Max: {max(values)}")
    print(f"Min: {min(values)}")


array_practice()
