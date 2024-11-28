class Jar:
    def __init__(self, capacity = 12):
        capacity = int(input('What is the capacity of the jar?'))
        if capacity < 1:
            raise ValueError('Wrong capacity value')
        self._capacity = capacity
        self._n = int(input('How many cookies are in the jar?'))

    def __str__(self):
        return '🍪' * self._n

    def deposit(self, n):
        if self._n + n > self._capacity:
            raise ValueError('Exceed Capacity')
        self._n += n


    def withdraw(self, n):
        if self._n < n:
            raise ValueError('Not enough cookies')
        self._n -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._n


my_jar = Jar()
my_jar.deposit(3)
print(my_jar)
print(my_jar._capacity)
print(my_jar._n)