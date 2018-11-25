"""
Iterators are everywhere in Python. They are elegantly implemented within for loops, comprehensions, generators etc.
but hidden in plain sight.

Iterator in Python is simply an object that can be iterated upon.
An object which will return data, one element at a time.

Technically speaking, Python iterator object must implement two special methods,
__iter__() and __next__(), collectively called the iterator protocol.

An object is called iterable if we can get an iterator from it.
Most of built-in containers in Python like: list, tuple, string etc. are iterables.

The iter() function (which in turn calls the __iter__() method) returns an iterator from them.


"""

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration