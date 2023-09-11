
""""
A function- contains several commands that are grouped together under one name in such a way that it can be called from where and when it is needed.
Functions are used everywhere in Python.

A function's return value is the value that the function will return when it is called outside the function.

Pass by Object Reference:
When you pass a mutable object to a function, any changes made to the
object inside the function will be reflected in the original object because you are working with the same object reference.
Pass by Value:
When you pass an immutable object (e.g., numbers, strings, tuples) to a function,
a copy of the object is created within the function's scope. Any changes made to the object inside the function will not affect the original object.


The scope defines the accessibility of the python object. To access the particular variable in the code,
the scope must be defined as it cannot be accessed from anywhere in the program. The particular coding region where variables are visible is known as scope

The lifetime of a variable or object in Python is determined according to the following routine:
1. Creation: A variable or object is created when you first compare a value to it and use it. For example,
 when you define a variable or use a new object within the code, it is created at that moment.
2. Garbage Collection: In Python, there is a garbage collector that deals with locating and deleting variables and objects
 that are no longer needed. The time that a variable or an object will be deleted from the memory is not known in advance and depends on the system measurements, the use of the variable.

Division into functions (Function Scope):
When you define a variable inside a function, it is limited to being visible only inside the function. It exits the scope of the function when the function ends. 

Indentation:In Python is used to define the block scope of code. Whenever you use a scope case, such as inside a loop or function,
you should use indentation to mark the correct scope case level. When the scope case ends (for example, the end of the loop or function),
the indentation ends and the scope ends.

"""
import math
import random
def hello(name):
    print(f'hello {name}! great to see you')

def square(a,b,c):
    delta = b ** 2 - (4 * a * c)
    solution1 = ((b * -1) + math.sqrt(delta)) / (2 * a)
    solution2 = ((b * -1) - math.sqrt(delta)) / (2 * a)
    if solution1 == solution2:
        print("the solution is: " + str(solution1))
    else: 
        print(f'the solutions are {solution1} and {solution2}')

def random_number_int(a, b):
    if a > b:
        a, b = b, a 
    return random.randint(a, b)

def random_number_double(a, b):
    if a > b:
        a, b = b, a  
    return random.uniform(a, b)

"""
Recursion means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
it is a programming technique where a function calls itself within its own body. Recursion can be used when we have a problem or 
a task that can be solved by dividing it into smaller tasks, 
which flow into similar tasks with easier ones. That is, at each step of recursion, the problem is reduced and solved for smaller and simpler cases.

We will usually use recursion when we have a structure that consists of identical or similar parts,
and we would like to perform identical operations on each of the parts and combine the results to repeat the original structure, For example in the Fibonacci.

Using general loops will be more efficient in terms of runtime than using recursion in most cases. Recursion adds a load on the memory and the call to the functions
,where each call to the function creates a new frame of variables and stack.

"""


