
"""
1. Generator is a function that returns an iterator that produces a sequence of values when iterated over.
Generators are useful when we want to produce a large sequence of values, but we don't want to store all of them in memory at once.
Generator Functions are memory efficient, as they save a lot of memory while using generators. A normal function will return a sequence of items, 
but before giving the result, it creates a sequence in memory and then gives us the result, whereas the generator function produces one output at a time.

2. Generators are good to use in python because:
Infinite Sequence: As generators can only produce one item at a time, so they can present an infinite stream of data/sequence.
 Memory Efficient: Generator Functions are memory efficient, as they save a lot of memory while using generators.

 3. Assigning a generator to a variable is useful when you want to iterate over its values multiple times or when you want to pass it as an argument to a function.
By keeping a reference to the generator, you can control when and how you iterate over its values.

4. Generator functions are defined as the normal function, but to identify the difference between the normal function and generator function is that in the normal function,
 we use the return keyword to return the values, and in the generator function, instead of using the return, we use yield to execute our iterator.
  After returning the value from yield, it pauses the execution by saving the states. but when we usr return it returns the value and terminates the function.
"""

def numbers_up_to_n(N):
    for i in range(1, N + 1):
        yield i

gen = numbers_up_to_n(5)
for num in gen:
    print(num)

