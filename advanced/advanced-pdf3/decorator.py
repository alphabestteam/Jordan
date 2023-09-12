"""

1. a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.
The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.

2.  Decorators are to add additional functionality to a function without changing its code, which shortens the code and gives the possibility of reuse.
we using decorators to adapt function behavior for a variety of purposes: including authentication, measurement logic, and adding calls to logs.

What happens behind the scenes when you use Decorator is:
The decorator itself is a function that takes the function that is wrapped as a parameter. 
Inside the Decorator creates an additional function (the wrapper) that executes the original function and adds additional functionality to it.
The Decorator returns the newly created func (wrapper) to be used instead of the original function.

3. A function pointer is a concept in programming languages like C and C++. It is essentially a variable that can store the address of a function in memory. 
 you can pass them as arguments to other functions, return them from functions, and assign them to variables.
In Python, there aren't function pointers like there are in other programming languages like C or C++. 
In Python, functions are parametric objects, and can be passed as arguments to other functions to use as callback arguments.

4. '*args' and '**kwargs' are used in Python decorators when you want to create generic decorators that can work with functions that can accept a different number of arguments.
Using '*args' and '**kwargs' when writing a decorator, you can create generic decorators that can work with all types of functions, regardless of the amount or type of arguments they get. 

5. @property decorator: used to define getter methods for class attributes, effectively allowing you to create read-only properties. 
It helps you control access to attributes and add custom behavior when getting their values.
"""
import time
def timer_func(func):
    def wrapper_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.2f} seconds")
        return result
    return wrapper_func

@timer_func
def sum_many_numbers():
    sum =0
    for i in range (100000000):
        sum+=i
sum_many_numbers()



