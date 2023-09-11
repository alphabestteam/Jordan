
"""
Exceptions are events or objects in programming that represent unexpected or erroneous situations that can occur during the execution of a program.
Exceptions can occur for various reasons, such as division by zero, attempting to access a non-existent file, or invalid input. When an exception occurs,
it interrupts the normal flow of the program and provides information about the error, including its type and a traceback of where the error occurred.
To handle exceptions in your code, you can use a combination of try, except, and optionally finally blocks.

"""
try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    result = x / y
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    print(f"The result of {x} / {y} is {result}")
finally:
    print("Finished running")

"""
    List comprehension in Python is an easy and compact syntax for creating a list from a string or another list.
    It is a very concise way to create a new list by performing an operation on each item in the existing list. 
    The main use for these lists is to create new lists from existing lists or iterate over an existing list and return a new list of the items that meet certain conditions.

    their use is not mandatory and they are designed to facilitate programming and reading the code. 
    in simple and small cases you may not want to use them, but in more complex cases, using them can improve code readability and reduce code lines.
"""

from intermediate2 import Person
N = 5
squares_array = [x ** 2 for x in range(1, N+1)]
print(squares_array)  


persons = [Person(input("Enter name: "), int(input("Enter ID: ")), int(input("Enter age: "))) for i in range (N)]
persons_over_18 = [person for person in persons if person.get_age() > 18]
print("People over 18:")
for person in persons_over_18:
    print(f"Name: {person.get_name()}, ID:{person.get_id_number()} Age: {person.get_age()}")




