
"""
An iterator is an object that contains a countable number of values.
it is an object that can be iterated upon, meaning that you can traverse through all the values.
An iterable object is an object that implements __iter__, which is expected to return an iterator object.
An iterator object implements __next__, which is expected to return the next
element of the iterable object that returned it, and to raise an exception when no more elements are available.

lists, strings and dictionary are iterators

when we use del action inside object its delete the object or the value we use 'del' on

to make our object to be an iterator we have to use __iter__() and __next__() functions, as i explained before.
"""

class People:
    def __init__(self):
        self.list = ["jordan", "gilad", "ziv", "koral", "matan"]

    def AddPerson(self, name):
        self.list.append(name)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.list):
            result = self.list[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

people = People()
people.AddPerson("shahaf")
people.AddPerson("maya")
for name in people:
    print(name)






